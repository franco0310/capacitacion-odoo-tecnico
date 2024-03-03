# -*- coding: utf-8 -*-
{
    'name': "Motorcycle Registry",

    'summary': """
        Manage Registration of Motorcycles""",

    'description': """
        Motorcycle Registry
        ======================
        This Module is used to keep of the Motorcycle Registration and Ownership
        of each motorcycled of the brand.
    """,

    'author': "franco0310",
    'version': "0.0.1",
    'license': "OPL-1",
    'website': "https://github.com/franco0310/capacitacion-odoo-tecnico",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Kawiil",
    "application": True,
    
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
