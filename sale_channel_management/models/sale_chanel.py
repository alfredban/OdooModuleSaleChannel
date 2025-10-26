from odoo import models, fields, api

class SaleChanel(models.Model): 
 _name = 'sale.chanel'
 _description = 'sale chanel'

 name = fields.Char(string='name', required = True)
 code = fields.Int(string="code", required = True)