# -*- coding: utf-8 -*-
# from odoo import http


# class LibrosAbl(http.Controller):
#     @http.route('/libros_abl/libros_abl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libros_abl/libros_abl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libros_abl.listing', {
#             'root': '/libros_abl/libros_abl',
#             'objects': http.request.env['libros_abl.libros_abl'].search([]),
#         })

#     @http.route('/libros_abl/libros_abl/objects/<model("libros_abl.libros_abl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libros_abl.object', {
#             'object': obj
#         })
