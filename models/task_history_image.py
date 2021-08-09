# -*- coding: utf-8 -*-

"""
All models from Task History image module
"""

from odoo import models, fields

class TaskHistoryImage(models.Model):
	"""
	Class Task History image 
	"""
	_name = "lsv_project.task_history_image"

	image = fields.Binary(string='Image')

	task_history_id = fields.Many2one('lsv_project.task_history',
									  required=True)