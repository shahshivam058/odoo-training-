# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Result_Wizard(models.TransientModel):
    _name='result.wizard'
    _description='this class is transieant model'

    total_attendance=fields.Integer()   
    exam_id = fields.Many2one('exam',string="Exam Type",ondelete='restrict')
    marks=fields.Integer()

    @api.multi
    def  action_get_exam(self):
        exam_result=self.env['students'].browse(self.env.context.get('active_ids'))
        exam_result.write({'total_attendance':self.total_attendance,'exam_id':self.exam_id.id,'marks':self.marks})
        return exam_result

