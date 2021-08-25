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

	start_on = fields.Date(string='Start Date',
						   required=True)
	end_on = fields.Date(string='End Date',
						 required=True)
	responsible_id = fields.Many2one('res.partner',
									 required=True,
									 domain=[('is_resident','=', 'True')])
	project_id = fields.Many2one('project.project',
								 required=True)
	task_ids = fields.Many2many('project.task',
							   required=True)