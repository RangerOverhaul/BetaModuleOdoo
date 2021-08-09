# -*- coding: utf-8 -*-

from odoo import models, fields

class ResidentRole(models.Model):


	_name = "lsv_project.resident_role"

	_rec_name = "name"

	name = fields.Char(string='Name',
					   required=True)