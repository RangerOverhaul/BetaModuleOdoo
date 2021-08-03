# -*- coding: utf-8 -*-

"""
All models from addendum_description module
"""

from odoo import models, fields

class AddendumDescription(models.Model):
	"""
	Addendum description class
	"""
	_name = "lsv_project.addendum_description"
	_rec_name = 'name'
	name = fields.Char(string='Nombre',
		               required=True)
