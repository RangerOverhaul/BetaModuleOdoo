# -*- coding: utf-8 -*-

"""
All models from bail module
"""

from odoo import models, fields

class Bail(models.Model):
    """
     Bail class
    """
    _name = "lsv_project.bail"
    _rec_name = "number"
    number = fields.Char(string='Number',
			             required=True)
    issue_date = fields.Date(string='Issue Date',
			                 required=True)
    expired_at = fields.Date(string='Expired at',
    						 required=True)
    insurer_id= fields.Many2one('res.partner',
				                string='Insurer',
				                required=True)
    project_id = fields.Many2one('project.project',
				                 string='Project',
				                 required=True)
    endorsement_ids = fields.One2many('lsv_project.endorsement',
    								  'bail_id',
				                      string='Endorsement',
				                      required=True)

