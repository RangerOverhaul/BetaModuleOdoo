# -*- coding: utf-8 -*-

"""
All models from Res Config Settings module
"""

from odoo import models, fields


class ResConfigSettings(models.TransientModel):

	"""
	Res Config Settings Class
	"""

	_inherit = 'res.config.settings'

	google_maps_api_key = fields.Char(string='Google Maps Api Key')