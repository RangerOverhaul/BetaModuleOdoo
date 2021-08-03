#-*- coding: utf-8 -*-

from odoo import models, fields
"""
All models froms endorsement module
"""


class EndorsementReason(models.Model):
	"""
	Endorsement class
	"""
	_name = "lsv_project.endorsement_reason"
	_rec_name = 'reason'
	reason = fields.Char(string='Nombre',
			   	         required=True)
