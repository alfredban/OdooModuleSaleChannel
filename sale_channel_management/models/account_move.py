from odoo import models, fields, api

class AccountMove(models.Model):

    _inherit = "account.move" 
     
    sale_channel_id = fields.Many2one(comodel_name ='sale.channel', string="Sale Channel", readonly = True, stored = True)
    