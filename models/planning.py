# -*- coding: utf-8 -*-

"""
All models from Planing module
"""

from odoo import models, fields

class Planning(models.Model):
	"""
	Planing Class
	"""

	_name = "lsv_project.planning"

	_rec_name = "state"

	state = fields.Selection([
		('pending','Pending'),
		('active','Active'),
		('finished','Finished'),
	])

	start_on = fields.Date(string='Date',
						   required=True)
	end_on = fields.Date(string='Date',
						 required=True)
	responsible_id = fields.Many2one('res_partner',
									 required=True)
	project_id = fields.Many2one('project.project',
								 required=True)
	task_id = fields.Many2many('project.task',
							   required=True)