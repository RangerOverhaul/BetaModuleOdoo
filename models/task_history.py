# -*- coding: utf-8 -*-

"""
All models from Task History image module
"""

from odoo import models, fields

class TaskHistory(models.Model):

	_name = 'lsv_project.task_history'

	_rec_name = "date"

	date = fields.Date(string='Date',
					   required=True)
	time = fields.Char(string='Trime',
					   required=True)
	comments = fields.Text(string='Comments')
	latitude = fields.Float(string='Latitude',
							required=True)
	longitude = fields.Float(string='Longitude',
							 required=True)
	state = fields.Selection([
		('normal','Normal'),
		('done','Done'),
		('blocked','Bloked')
	])
	task_id = fields.Many2one('project.task',
							  required=True)
	task_history_image_ids = fields.One2many('lsv_project.task_history_image',
											 'task_history_id')