# -*- coding: utf-8 -*-

"""
All models from QR Code module
"""

from odoo import models, fields
import random


class QrCode(models.Model):
	"""
	This model service qr codes for tasks
	and projects
	start, stop=None _int=int
	"""

	def _compute_qr_token(self):
		return random.randrange(1000000,9999999,2)

	_name  = "lsv_project.qr_code"

	_rec_name = "code"

	code = fields.Binary(string='Qr Code',
						 required=False)
	filename = fields.Char(string='Filename',
						   required=False)
	token = fields.Integer(string='Token',
						  default=_compute_qr_token)

