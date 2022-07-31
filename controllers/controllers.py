# -*- coding: utf-8 -*-
from odoo import http

# class MethodNoteLinePosProducto(http.Controller):
#     @http.route('/method_note_line_pos_producto/method_note_line_pos_producto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_note_line_pos_producto/method_note_line_pos_producto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_note_line_pos_producto.listing', {
#             'root': '/method_note_line_pos_producto/method_note_line_pos_producto',
#             'objects': http.request.env['method_note_line_pos_producto.method_note_line_pos_producto'].search([]),
#         })

#     @http.route('/method_note_line_pos_producto/method_note_line_pos_producto/objects/<model("method_note_line_pos_producto.method_note_line_pos_producto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_note_line_pos_producto.object', {
#             'object': obj
#         })