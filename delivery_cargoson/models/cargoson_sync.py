from odoo import fields, models, api
import logging
logger = logging.getLogger(__name__)


def get_cron_time_limit():
    from odoo.tools import config
    limit_time_real_cron = config['limit_time_real_cron']
    if limit_time_real_cron <= 0:
        limit_time_real_cron = 900  # default to odoo.sh default
    return limit_time_real_cron


class CargosonSyncParcelMachine(models.Model):
    _name = 'cargoson.sync.parcel.machine'
    _description = 'Cargoson Parcel Machine update task'

    _sql_constraints = [
        ('unique_queue_item', 'UNIQUE(delivery_carrier_id, country_id)', 'Duplicate queue item')
    ]

    delivery_carrier_id = fields.Many2one(
        'delivery.carrier', string='Delivery carrier', ondelete='cascade', required=True)
    country_id = fields.Many2one('res.country', 'Country')

    @api.model
    def queue(self, delivery_carrier_id, country_id):
        self._cr.execute(
            """
                INSERT INTO {table} (delivery_carrier_id, country_id, create_date, write_date)
                VALUES (%s, %s, NOW(), NOW())
                ON CONFLICT (delivery_carrier_id, country_id) DO NOTHING
            """.format(table=self._table),
            (delivery_carrier_id, country_id))
        return self._cr.rowcount == 1

    def complete(self):
        self.unlink()
