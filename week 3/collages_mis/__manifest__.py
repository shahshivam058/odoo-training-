# -*- coding: utf-8 -*-

{
    'name': "Collages Mis",
    'description': """
        this module will give all informatation about collage mis and students
    """,
    'author': "shivam shah",
    'category': 'mis',
    'version': '0.1',
    'depends': ['base','website'],
    'data': [
        'security/collage_mis_security.xml',
        'security/ir.model.access.csv',
        'wizard/result_wizard_view.xml',
        'views/collage_mis_views.xml',
        'views/templates.xml',
        'data/collages_data.xml',
        'report/collage_mis_report.xml',
     ],
     'demo':[
        'data/collage_demo.xml'
     ],
    'installable':True,
    'application':True,
    'auto_install':True,
}