from odoo import models, fields, api

class SaleChannel(models.Model): 
 _name = 'sale.channel'
 _description = 'sale channel'

 name = fields.Char(string='name', required = True)
 code = fields.Int(string="code", required = True)