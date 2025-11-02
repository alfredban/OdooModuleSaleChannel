from odoo import models, fields, api

class SaleChannel(models.Model):

    _name = 'sale.channel' 
    _description = 'sale channel' 

    name = fields.Char(string='name', required = True) 
    code = fields.Integer(string="code", required = True) 
    
    
    #Relaciones
    warehouse_id = fields.Many2one( #Relacion con el deposito 
         comodel_name ='stock.warehouse', 
         string ='Deposit', required = True, 
    )
     
    invoice_journal_id = fields.Many2one( 
        comodel_name = 'account.journal', #Relacion con el diario de facturacion de cada canal 
        string = 'Invoice journal', required = True, 
    )
    
    