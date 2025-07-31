
{
    'name': 'Student Information',
    'summary': '''Student Information''',
    'description': '''Student Information''',
    'version': '18.0.1.0.0',
    'category': '',
    'license': 'LGPL-3',
    'author': 'Aktiv Software',
    'website': 'http://www.aktivsoftware.com',
    'depends': ["contacts"],
    'data': [
        #data
        #views
        'security/ir.model.access.csv',
        'views/student_information_views.xml',
        'views/education_info_views.xml',
        'views/education_tag_views.xml',
        'views/res_parther_views.xml',

        #wizard
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
