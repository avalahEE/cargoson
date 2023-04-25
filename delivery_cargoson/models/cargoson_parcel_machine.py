import datetime
import time

from odoo import fields, models, api
from .cargoson_sync import get_cron_time_limit
from .schema import ParcelMachines

import logging
logger = logging.getLogger(__name__)


class CargosonParcelMachine(models.Model):
    _name = 'cargoson.parcel.machine'
    _description = 'Cargoson parcel machine'

    _sql_constraints = [(
        'unique_machine', 'UNIQUE(delivery_carrier_id, machine_id)',
        'Parcel Machines must be unique for each Cargoson Shipping Method configuration')]

    delivery_carrier_id = fields.Many2one(
        'delivery.carrier', string='Delivery carrier', ondelete='cascade', required=True)

    machine_id = fields.Integer('Machine ID')
    reference = fields.Char('Reference')
    name = fields.Char('Name')
    carrier_name = fields.Char('Carrier name')
    carrier_id = fields.Integer('Carrier ID')
    carrier_reg_no = fields.Char('Carrier Reg. No')
    country_id = fields.Many2one('res.country', 'Country')
    city = fields.Char('City')
    address = fields.Char('Address')
    postcode = fields.Char('Zip')

    prune = fields.Boolean('This record is OK to delete')

    @api.model
    def cron_sync_parcel_machines(self):
        now = fields.Datetime.now()
        threshold = datetime.timedelta(days=1)

        cargoson_providers = self.env['delivery.carrier'].search([('delivery_type', '=', 'cargoson')])
        for record in cargoson_providers:
            for country in record.cargoson_parcel_machine_country_ids:
                dataset_timestamp = self.get_dataset_timestamp(record.id, country.id)
                if dataset_timestamp is None or now - dataset_timestamp >= threshold:
                    queued = self.env['cargoson.sync.parcel.machine'].queue(record.id, country.id)
                    if queued:
                        logger.info('Queued Parcel Machine task: %s (%s)', record.name, country.code)
                    else:
                        logger.info('Parcel Machine task already in queue: %s (%s)', record.name, country.code)

    @api.model
    def cron_sync_parcel_machine(self):
        queue = self.env['cargoson.sync.parcel.machine'].search([])
        if len(queue) == 0:
            return

        limit_time = get_cron_time_limit()
        logger.info('Start Parcel Machines sync (limit_time_real_cron=%ss)', limit_time)
        start = time.time()

        query = """
            INSERT INTO {table} (
                delivery_carrier_id,
                machine_id,
                reference,
                name,
                carrier_name,
                carrier_id,
                carrier_reg_no,
                country_id,
                city,
                address,
                postcode,
                prune,
                create_date,
                write_date
            )
            VALUES {rows}
            ON CONFLICT (delivery_carrier_id, machine_id)
            DO UPDATE SET
                reference = EXCLUDED.reference,
                name = EXCLUDED.name,
                carrier_name = EXCLUDED.carrier_name,
                carrier_id = EXCLUDED.carrier_id,
                carrier_reg_no = EXCLUDED.carrier_reg_no,
                country_id = EXCLUDED.country_id,
                city = EXCLUDED.city,
                address = EXCLUDED.address,
                postcode = EXCLUDED.postcode,
                prune = EXCLUDED.prune,
                write_date = NOW()
        """
        row_format = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),NOW())"

        for queue_item in queue:
            # Mark existing records for pruning
            self._cr.execute(
                """
                    UPDATE {table} SET prune = true
                    WHERE delivery_carrier_id = %s AND country_id = %s
                """.format(table=self._table), (queue_item.delivery_carrier_id.id, queue_item.country_id.id))

            logger.info('%s: Syncing Cargoson parcel machines', queue_item.country_id.code)
            vals, num_machines = self._get_parcel_machines_rows(queue_item.delivery_carrier_id, queue_item.country_id)
            logger.info('%s: Received %s parcel machines', queue_item.country_id.code, num_machines)
            if len(vals) > 0:
                sql = query.format(table=self._table, rows=', '.join([row_format] * num_machines))
                self._cr.execute(sql, vals)

            # Prune records that no longer exist
            self._cr.execute(
                """
                    DELETE FROM {table} WHERE prune = true AND delivery_carrier_id = %s
                    AND country_id = %s
                """.format(table=self._table), (queue_item.delivery_carrier_id.id, queue_item.country_id.id))
            if self._cr.rowcount:
                logger.info('Pruned %s records', self._cr.rowcount)

            queue_item.complete()

            if limit_time > 0 and time.time() - start > limit_time - 60:
                logger.warning('Reached close to thread time limit (%ss), continuing next interval', limit_time)
                break

        logger.info('Parcel Machines sync completed in %ss', round(time.time() - start, 3))

    @api.model
    def get_dataset_timestamp(self, delivery_carrier_id, country_id):
        self._cr.execute(
            'SELECT MIN(write_date) FROM {table} WHERE delivery_carrier_id = %s AND country_id = %s'.format(
                table=self._table),
            (delivery_carrier_id, country_id))
        (timestamp,) = self._cr.fetchone()
        return timestamp

    @api.model
    def _get_parcel_machines_rows(self, provider, country):
        result = provider.cargoson_api_get('parcelMachines', dict(country=country.code))
        vals = list()
        for item in result:
            machine = ParcelMachines.from_dict(item)
            vals.append(provider.id)
            vals.append(machine.id)
            vals.append(machine.reference)
            vals.append(machine.name)
            vals.append(machine.carrier_name)
            vals.append(machine.carrier_id)
            vals.append(machine.carrier_reg_no)
            vals.append(country.id)
            vals.append(machine.address_row_1)
            vals.append(machine.city)
            vals.append(machine.postcode)
            vals.append(False)  # prune
        return vals, len(result)
