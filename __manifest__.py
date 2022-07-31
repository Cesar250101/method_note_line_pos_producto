# -*- coding: utf-8 -*-
{
    'name': "method_note_line_pos_producto",

    'summary': """
            Reemplaza el nombre del productos por la nota
            de la linea del producto, para que funcione esta modulo 
            el POS debe estar configurado como restaurent
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Method ERP",
    'website': "https://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

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
    'qweb': [
        'static/src/xml/layout.xml',
        #'static/src/xml/client.xml',
        #'static/src/xml/payment.xml',
    ],    
}