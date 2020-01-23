# -*- coding: utf-8 -*-

from odoo import models,fields,api


class Faculty(models.Model):
     _name = 'faculty'
     _inherit = "department"
     _rec_name = "faculty_name"
     _description = "this module will give the informatation about the faculty"

     faculty_name = fields.Char(required="true")
     mobile_no = fields.Char()
     collage_joining_date = fields.Date()
     email_id = fields.Char()

class Other_Info(models.Model):
    _inherit = "students"

    father_name = fields.Char()
    mother_name = fields.Char()
    date_of_birth = fields.Datetime()
    division = fields.Char()
    
class Fees(models.Model):
    _name = "fees"
    _inherits = {'collage':'collages_id'}
    _description = "this module will give informatation about fees structure"
    _rec_name = 'collages_id'

    tution_fees = fields.Integer()
    extra_fees = fields.Integer()
    diposit = fields.Integer()
    last_date = fields.Date()
    collages_id = fields.Many2one("collage",string="collage name",ondelete='restrict',required=True)
    total_fees = fields.Integer(compute='_compute_total_fees')
    
    @api.multi
    def _compute_total_fees(self):
        for i in self:
            i.total_fees=i.tution_fees+i.extra_fees+i.diposit
