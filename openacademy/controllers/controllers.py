# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class OpenacademyBasic(http.Controller):

    @http.route('/hello/', type='http', auth='public')
    def test_hello(self, **kw):
        # key word arguments
        return '<h1> Hello World </h1>'

    @http.route('/hello/world_1', type='http', auth='public')
    def test_hello2(self):
        return '<b><i>Hello World</i></b>'

    @http.route('/static_page', type='http', auth='public', website=True)
    def static_controller(self):
        return request.render('openacademy.static_page', {})

    @http.route(['/dynamic_page/', '/dynamic_page/<int:any_number>'], type='http', auth='user', website=True)
    def dynamic_controller(self, any_number=None):
        print('\n\n\n ----------- any_number :', any_number)
        return request.render('openacademy.dynamic_page', {
            'user_rec': request.env.user,
            'my_fnc': self.test_string,
            'user_ids': [1,2,3,4,5,6,7],
            'link': '/static_page',
            'link_class': 'btn-success',
        })


    @http.route('/openacademy/courses', type='http', auth='public', website=True)
    def course_main_controller(self):
        courses = request.env['openacademy.course'].sudo().search([])
        return request.render("openacademy.courses", {
            'courses': courses
        })

    @http.route('/openacademy/courses/<model("openacademy.course"):course>', type='http', auth='public', website=True)
    def course_desctiption_controller(self, course=None):
        return request.render("openacademy.course_details", {
            'course': course.sudo()
        })

    def test_string(self):
        return 'This is test string from function'


# class Openacademy(http.Controller):
#     @http.route('/openacademy/openacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy/openacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy.listing', {
#             'root': '/openacademy/openacademy',
#             'objects': http.request.env['openacademy.openacademy'].search([]),
#         })

#     @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy.object', {
#             'object': obj
#         })
