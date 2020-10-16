# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """Manage your Course, Session, Attendee""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Rational",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web_gantt', 'web_map', 'web_cohort', 'web_dashboard', 'website'],
    'application' : True,

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'wizard/wizard_views.xml',
        'views/templates.xml',
        'views/snippets.xml',
        'views/report.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
