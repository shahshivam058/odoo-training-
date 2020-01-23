# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions,_


class Students(models.Model):
    _name = 'students'
    _rec_name = "name"
    _description = "this class will give informatation about the collage students "
    _inherit = 'mail.thread'
    
    name = fields.Char(required=True,size=10)
    enrollment_no = fields.Char(compute='_compute_enrollment_no')
    semester = fields.Integer()
    email_id = fields.Char()
    mobile_no = fields.Char()
    current_address = fields.Text()
    premeanent_address = fields.Text()
    same_as_permeneant = fields.Boolean()
    total_attendance = fields.Integer(size=3)
    admission_year = fields.Date()
    passing_year = fields.Date()
    color = fields.Integer()
    marks = fields.Integer()
    state = fields.Selection([('add_new','ADD NEW'),
                            ('ragister',"RAGISTRATION"),
                            ('ragistration_sucessful','RAGISTRATION DONE'),
                            ('cancell','CANCEL')],default='add_new')
    department_id = fields.Many2one("department",string="Department Name",ondelete='restrict')
    collage_id = fields.Many2one('collage',"collages",ondelete='restrict')
    total_students=fields.Integer(compute='_compute_total_students')
    course_id = fields.Many2one("courses","course",ondelete='restrict')
    exam_id = fields.Many2one('exam',string="exam type",ondelete='restrict')

    _sql_constraints = [('student_name_unique','UNIQUE(name)','student name should be unique')]

    @api.depends('name','admission_year')
    def _compute_enrollment_no(self):
        for record in self:
            s =""
            date=str(record.admission_year)
            r=date.split("-")
            date=s.join(r)
            record.enrollment_no="%s"%record.name+date

    @api.constrains('semester')
    def _check_semester(self):
        for record in self:
            if record.semester > 8:
                raise exceptions.ValidationError("enter semester number carefully")

    def add_new(self):
        self.write({'state':'add_new'})

    def action_ragister(self):
        self.write({'state':'ragister'})

    def ragistration_sucessful(self):
        self.write({'state':'ragistration_sucessful'})

    def action_cancell(self):
        self.write({'state':'cancell'})

    @api.multi
    def _compute_total_students(self):
        for record in self:
            record.total_students=self.env['students'].search_count([('exam_id', '=', 'mid sem')])

    def action_total_students(self):
        return {
                'type': 'ir.actions.act_window',
                'name': 'total students',
                'view_mode': 'tree',
                'res_model': 'students',
                'domain': [('exam_id', '=', 'mid sem')]
        }

class Department(models.Model):
    _name = "department"
    _description = "this is the department class"
    _rec_name = "department_name"

    department_name = fields.Char()
    head_of_department = fields.Char()
    department_code = fields.Integer(default="16")
    department_test=fields.Date()
    student_ids = fields.One2many("students","department_id",copy=True)

class Collage(models.Model):
    _name = "collage"
    _description = "this module will give informatation about diffreant modules"
    _rec_name="name"

    name = fields.Char(help="collage name",copy=False)
    principal_name = fields.Char(copy=False)
    department_ids = fields.Many2many('department','department_collage_informatation_rel','product_id','department_id')

class Course(models.Model):
    _name = "courses"
    _description = "this class will give informatation about the "
    _rec_name = "name"

    name = fields.Char()

class Exam(models.Model):
    _name='exam'
    _description = "this class is about the student student exam"
    _rec_name = 'exam_type'

    exam_type = fields.Char(default='mid sem')
    exam_start_date = fields.Date()
    exam_end_date = fields.Date()
    department_id = fields.Many2one('department', string='department name', ondelete='restrict')
    collages_id = fields.Many2one("collage",string="collage name",ondelete="restrict")
    allow_exam = fields.Integer(compute='_compute_allow_exam',string='Student Allowed to sit in exam')


    @api.multi
    def _compute_allow_exam(self):
        for stu_exam in self:
            stu_exam.allow_exam=self.env['students'].search_count([("total_attendance", '>', 75)])

    @api.onchange('exam_end_date')
    def _onchange_date(self):
        for record in self:
            if record.exam_start_date > record.exam_end_date:
                return {
                    'warning': {
                        'title': "mistake while selection of date",
                        'message': "start date can not be greter than end date",
                    }
                 }

    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        default['exam_type'] = u"{} (copy)".format(self.exam_type)
        return super(Exam, self).copy(default)

class result(models.Model):

    _name = 'result'
    _description = 'this class will give informatation about result of students '

    department_id = fields.Many2one("department",string="Department Name",ondelete='restrict')
    collage_id = fields.Many2one('collage',"collages",ondelete='restrict')
    course_id = fields.Many2one("courses","course",ondelete='restrict')
    exam_id = fields.Many2one('exam',string="exam type",ondelete='restrict')
    result = fields.Char()
