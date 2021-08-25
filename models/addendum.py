# -*- coding: utf-8 -*-

"""
All models from Addendum module
"""
import logging
from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
_logger = logging.getLogger('__name_')

class Addendum(models.Model):
	"""
	Addendum class
	"""
	_name = "lsv_project.addendum"
	
	_rec_name = "number"

	number = fields.Char(string='Numer',
					     required=True)
	comments = fields.Text(string='Comments',
						   required=False)
	start_at = fields.Date(string='Start At',
		                   required=True)
	end_at = fields.Date(string='End At',
		  				 required=True)
	addendum_date = fields.Date(string='Addendum Date',
								required=False)
	project_id = fields.Many2one('project.project',
								 string='Project',
								 required=True)
	addendum_description_id = fields.Many2one('lsv_project.addendum_description',
											  string='Description',
											  required=True)

	@api.onchange('start_at')
	def _onchange_start_at(self):
		if self.start_at and self.start_at< datetime.now().date():
			self.start_at = False
			raise ValidationError("The field Start At must be greater than current date")
			
	@api.onchange('end_at')
	@api.depends('start_at')
	def _onchange_end_at(self):
		if self.end_at and self.start_at and  self.end_at <= self.start_at:
			raise ValidationError("The filed End At date must be greater than Start At")

	@api.onchange('addendum_date')
	@api.depends('start_at','end_at')
	def _onchange_addendum_date(self):
		if self.start_at and self.end_at and (self.addendum_date or self.addendum_date >self.end_at):
			raise ValidationError("The dield Addendum Date must be greater than start at and lesser than End At")


	def _validate_number(self,number,project_id,id=None):
		counter = self.env['lsv_project.addendum'].search_count([
				('project_id','=',project_id),
				('number','ilike',number)
			])
		if id is not None:
			params.append(('id','!=',id))
		counter = self.env['lsv_project.addendum'].search_count(params)
		if counter > 0:
			raise ValidationError("The number of Addendum already exists")

	@api.model
	def create(self, vals):
		"""
		override default create method
		"""
		project_id = vals.get('project_id', False)
		number = vals.get('number',False)
		_validate_number(number,project_id)
		return super(Addendum, self).create(vals)