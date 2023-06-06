from odoo import fields, models, api
from enum import Enum
from .cargoson_sync import get_cron_time_limit
import time
import json
import logging
logger = logging.getLogger(__name__)


class TaskResult(Enum):
    OK = 0,
    ERR = 1,
    RETRY = 2,


class CargosonQueueTask(models.Model):
    _name = 'cargoson.queue.task'
    _description = 'Async queue task'

    name = fields.Char('Name', required=True)
    res_id = fields.Integer('Resource ID', required=True)
    res_name = fields.Char('Model name', required=True)
    method = fields.Char('Method name', required=True)
    params_json = fields.Text('Method parameters')
    num_tries = fields.Integer(
        'Number of tries', required=True, default=0, help='Number of times this task has been executed')

    state = fields.Selection([
            ('pending', 'Pending'),
            ('in_progress', 'In progress'),
            ('completed', 'Completed'),
            ('error', 'Error'),
        ], string='State', required=True, default='pending')

    @api.model_create_multi
    def create(self, vals_list):
        def exists(vals):
            count = self.env['cargoson.queue.task'].search_count([
                ('name', '=', vals.get('name')),
                ('res_id', '=', vals.get('res_id')),
                ('res_name', '=', vals.get('res_name')),
                ('method', '=', vals.get('method')),
                ('state', '=', 'pending'),
            ])
            return count > 0
        vals_list = [vals for vals in vals_list if not exists(vals)]
        return super().create(vals_list)

    @api.model
    def execute_instance_tasks(self, res_id: int, res_name: str, include_error=False):
        tasks = self.env['cargoson.queue.task'].search([
            ('res_id', '=', res_id),
            ('res_name', '=', res_name),
            ('state', '=', 'pending')
        ])
        logger.info('Start processing instance queued tasks (include_error=%s)', include_error)
        if include_error:
            tasks = tasks.filtered(lambda task: task.state in ['pending', 'error'])
        if len(tasks) == 0:
            return

        limit_time = get_cron_time_limit()
        logger.info('Processing instance queued tasks (limit_time_real_cron=%ss): %s', limit_time, len(tasks))
        start = time.time()

        task_results = []

        for record in tasks:
            # consume queue item
            record.write(dict(state='in_progress'))
            record.flush()

            instance = record.validate()
            if not instance:
                record.write(dict(state='error'))
                record.flush()
                task_results.append({'id': record.id, 'name': record.name, 'result': TaskResult.ERR})
                continue

            record.execute(instance)
            task_results.append({'id': record.id, 'name': record.name, 'result': TaskResult.OK})

            if limit_time > 0 and time.time() - start > limit_time - 60:
                logger.warning('Reached close to thread time limit (%ss), continuing next interval', limit_time)
                break

        logger.info('Queue processed in %ss and returning tasks: %s', round(time.time() - start, 3), task_results)
        return task_results

    @api.model
    def cron_execute_tasks(self):
        queued = self.env['cargoson.queue.task'].search([('state', '=', 'pending')])
        if len(queued) == 0:
            return

        limit_time = get_cron_time_limit()
        logger.info('Start processing queued tasks (limit_time_real_cron=%ss): %s', limit_time, len(queued))
        start = time.time()

        for record in queued:
            # consume queue item
            record.write(dict(state='in_progress'))
            record.flush()

            instance = record.validate()
            if not instance:
                record.write(dict(state='error'))
                record.flush()
                continue

            record.execute(instance)

            if limit_time > 0 and time.time() - start > limit_time - 60:
                logger.warning('Reached close to thread time limit (%ss), continuing next interval', limit_time)
                break

        logger.info('Queue processed in %ss', round(time.time() - start, 3))

    def execute(self, instance):
        self.ensure_one()
        params = dict()
        if self.params_json:
            try:
                decoded = json.loads(self.params_json)
                if isinstance(decoded, dict):
                    params = decoded
            except Exception:  # noqa
                pass
        res = getattr(instance, self.method)(self, **params)
        self.update_state(res)

    def validate(self):
        self.ensure_one()

        if self.res_name not in self.env:
            logger.warning('Task references a non-existing model: %s', self.res_name)
            return None

        instance = self.env[self.res_name].browse([self.res_id])
        if not instance:
            logger.warning(
                'Task references a non-existing instance: %s(id=%s)',
                self.res_name, self.res_id)
            return None

        if not hasattr(instance, self.method):
            logger.warning(
                'Task references a non-existing method: %s(id=%s).%s',
                self.res_name, self.res_id, self.method)
            return None

        return instance

    def update_state(self, state):
        self.ensure_one()
        if not isinstance(state, TaskResult):
            return

        vals = dict(num_tries=self.num_tries + 1, state='pending')
        if state == TaskResult.OK:
            vals['state'] = 'completed'
        elif state == TaskResult.ERR:
            vals['state'] = 'error'
        elif state == TaskResult.RETRY:
            vals['state'] = 'pending'

        self.write(vals)
        self.flush()
