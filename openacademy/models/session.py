# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'openacademy.session'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'openacademy_session'

    name = fields.Char(string='Session', required=True)
    start_date = fields.Date("Start Date", default=fields.Date.today)
    stop_date = fields.Date("Stop Date")
    duration = fields.Float(string="Duration")
    seats = fields.Integer("Number of Seats")
    active = fields.Boolean(default=True, tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done')], required=True, default='draft', tracking=True)
    instructor_id = fields.Many2one('res.partner')
    instructor_mail = fields.Char(related='instructor_id.email', string="Instructor mail")
    course_id = fields.Many2one('openacademy.course', string='Course')
    attende_ids = fields.Many2many('res.partner')
    attendee_count = fields.Integer(compute='_calculate_occupation', store=True, compute_sudo=True)
    occupation = fields.Float(compute='_calculate_occupation', compute_sudo=True)

    @api.model
    def create(self, values):
        if not values.get('instructor_id'):
            values['active'] = False
        created_session = super().create(values)
        return created_session

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {}, name=_("%s (copy)") % self.name)
        return super().copy(default=default)

    def write(self, values):
        # other code
        return super().write(values)


    # Stop date should be after start date
    @api.depends('start_date', 'stop_date')
    def _onchange_dates(self):
        if self.stop_date < self.start_date:
            raise ValidationError(_("Stop date cannot be before start date"))

    def unlink(self):
        for session in self:
            if session.attendee_count:
                raise ValidationError(_("You can not delete the session having attendees"))
        return super().unlink()

    @api.depends('attende_ids', 'seats')
    def _calculate_occupation(self):
        for session in self:
        	if session :
		    session.attendee_count = len(session.attende_ids)
		    if session.seats:
		        session.occupation = session.attendee_count * 100 / session.seats
		    else:
		        session.occupation = 0.0

    def print_sessions(self):
        lumber_partners = self.env['res.partner'].search([('name', '=', 'Lumber Inc')], limit=5)

    def confirm_session(self):
        self.state = 'confirmed'

    def done_session(self):
        self.state = 'done'
