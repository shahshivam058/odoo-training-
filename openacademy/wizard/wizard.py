# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CourseWizard(models.TransientModel):

    _name = 'openacademy.wizard'
    _description = 'openacademy_inherted_wizard'

    name = fields.Char(string="Course Name")

    def add_course(self):
        course = self.env['openacademy.course']
        selected_session = self.env['openacademy.session'].search([('id', 'in', self.env.context.get('active_ids'))])
        for wiz_rec in self:
            created_course = course.create({'name': wiz_rec.name})
            selected_session.write({'course_id': created_course.id})
