# -*- coding: utf-8 -*-

"""
All models from policy  module
"""

from odoo import models, fields

class Policy(models.Model): 
	"""
        Policy class
        """
	_name = 'lsv_project.policy'
	number = fields.Char(string='Number',
			     		 required=True)
	project_id = fields.Many2one('project.project',
			                     string='Project',
				                 required=True)
	policy_type_id = fields.Many2one('lsv_project.policy_type',
					  			     string='Policy',
					  				 required=True)
