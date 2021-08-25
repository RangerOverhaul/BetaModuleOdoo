# -*- coding: utf-8 -*-

"""
All models from Project module
"""

from odoo import models, fields

class Project(models.Model):

	_inherit = "project.project"
	_name ="project.project"


	def _get_planning_count(self):
		for project in self:
			project.planning_count = len(project.planning_ids)

	resident_id = fields.Many2one('res.partner',
								  required=False,
								  domain=[('is_resident','=', 'True')])
	qr_code_id = fields.Many2one('lsv_project.qr_code',
								 required=False)
	addendum_ids = fields.One2many('lsv_project.addendum',
								   'project_id')
	policy_ids = fields.One2many('lsv_project.policy',
								 'project_id')
	bail_ids = fields.One2many('lsv_project.bail',
							   'project_id')
	planning_id = fields.One2many('lsv_project.planning',
								  'project_id')
	subprojects_ids = fields.One2many('lsv_project.subproject',
								      'project_id')
	planning_count = fields.Integer(string='Plannings counter',
									compute=_get_planning_count)