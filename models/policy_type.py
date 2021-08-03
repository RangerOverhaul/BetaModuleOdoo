# -*- coding: utf-8 -*-

"""
All models from policy_types module
"""

from odoo import models, fields

class PolicyType(models.Model):
        """
        police type  class
        """
        _name = "lsv_project.policy_type"
        _rec_name = 'name'
        name = fields.Char(string='Nombre',
			   required=True)


