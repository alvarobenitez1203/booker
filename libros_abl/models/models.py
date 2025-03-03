# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libros_abl(models.Model):
    _name = 'libros_abl.libros_abl'
    _description = 'Módulo para crear libros'
 
    nombre = fields.Char(string='Nombre')
    autor = fields.Char(string='Autor')
    editorial = fields.Char(string='Editorial')
    publicacion = fields.Integer(string='Publicacion')
    regalo = fields.Boolean(string='Regalo')
