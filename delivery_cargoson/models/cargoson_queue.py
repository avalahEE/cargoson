from odoo import fields, models, api
from enum import Enum
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
    def cron_execute_tasks(self):
        # TODO: lock, execute, set state, unlock
        logger.info('Executing queue tasks')
