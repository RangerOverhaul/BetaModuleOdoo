# -*- coding: utf-8 -*-

"""
All models from Sub Project module
"""

from odoo import models, fields


class SubProject(models.Model):

	"""
	Sub Project class
	"""

	_name = "lsv_project.subproject"

	_rec_name = "name"

	name = fields.Char(string='Name',
					   required=True)
	project_id = fields.Many2one('project.project',
								 required=True)