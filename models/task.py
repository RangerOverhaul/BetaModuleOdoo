# -*- coding: utf-8 -*-

"""
All models from Task History image module
"""

from odoo import models, fields

class Task(models.Model):

	_inherit = 'project.task'
	_name = 'project.task'

	progress = fields.Float(string='Progress')

	task_history_map = fields.Char(string='Map')

	sub_project = fields.Many2one('lsv_project.subproject')
	# cambio de True a False
	qr_code = fields.Many2one('lsv_project.qr_code',
							  required=False)
	task_history_ids =fields.One2many('lsv_project.task_history',
									  'task_id')
	planning_ids = fields.Many2many('lsv_project.planning',
								    required=True)