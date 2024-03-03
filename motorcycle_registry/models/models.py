# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MotorcycleRegistry(models.Model):
     _name = 'motorcycle.registry'
     _description = 'Motorcycle Registry'
     _rec_name = 'registry_number'

     certificate_title = fields.Binary(string='Certificate Title')
     current_mileage = fields.Float(string='Current Mileage')
     first_name = fields.Char(string='First Name', required=True)
     last_name = fields.Char(string='Last Name', required=True)
     license_plate = fields.Char(string='License Plate')
     registry_date = fields.Date(string='Registry Date')
     registry_number = fields.Char(string='Registry Number', required=True)
     vin = fields.Char(string='VIN', required=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
