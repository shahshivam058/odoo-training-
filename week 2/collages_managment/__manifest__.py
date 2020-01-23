# -*- coding: utf-8 -*-
{
    'name': "Collages Managment",
    'description': """this module will give informataion about the collage managemen and it also include verious model releted to managment    """,
    'author': "shivam shah",
    'category': 'managment',
    'version': '1.0',
    'depends': ['base','collages_mis'],
    'data': [
       'security/ir.model.access.csv',
       'views/collage_managment_views.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':True,
}