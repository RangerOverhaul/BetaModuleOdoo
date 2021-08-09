# -*- coding: utf-8 -*-

"""
All models from Res Partner module
"""

from odoo import models, fields


class Partner(models.Model):

	"""
	Res Partner Class
	"""

	_inherit = "res.partner"
	
	identify_number = fields.Char(string='Identify Number',
								  required=False)
	is_insurer = fields.Boolean(string='Is Insurer',
								default=False)
	is_resident = fields.Boolean(string='Is Resident',
								 default=False)
	resident_role_id = fields.Many2one('lsv_project.resident_role',
									  required=False)
