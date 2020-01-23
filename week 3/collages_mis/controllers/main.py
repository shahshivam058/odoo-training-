# -*- coding: utf-8 -*-

from odoo import http

class Admin(http.Controller):
    @http.route('/collage/admin/', auth='public')
    def index(self,**kw):
        return "hello, students"

    @http.route('/collage/hostle/', auth='user')
    def hostle(self, **kw):
        return http.request.render('collages_mis.index', {
            'hostle_name': ["shri hostle", "vns hostle", "aadarsh hostle"],
        })

    @http.route('/collage/students/', auth='public',website=True)
    def students_display(self, **kw):
       Students = http.request.env['students']
       return http.request.render('collages_mis.students', {
           'studentss': Students.search([])
       })

    @http.route('/collage/department/',auth='public',website=True)
    def department(self,**kw):
        Departments=http.request.env['department']
        return http.request.render('collages_mis.department', {
           'departments': Departments.search([])
       })

    @http.route('/acad/<department_name>/',auth='public',website=True)
    def department_display(self,department_name):
        return '<h1>{}</h1>'.format(department_name)

    @http.route('/academy/<int:id>/', auth='public', website=True)
    def teacher(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/collage/<model("students"):student>/', auth='public', website=True)
    def student(self, student):
        return http.request.render('collages_mis.data', {
           'students': student
           })
