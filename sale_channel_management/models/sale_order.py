from odoo import models, fields, api

class SaleOrder(models.Model):

    _inherit = "sale.order" 
     
    sale_channel_id = fields.Many2one(comodel_name ='sale.channel', string="Sale Channel", required=True)
    
    
    #----- ONCHANGES ------#

    
    @api.onchange('sale_channel_id')
    def _on_change_sale_channel(self):
    
        if self.sale_channel_id:
            self.warehouse_id = self.sale_channel_id.warehouse_id
        else:
            self.warehouse_id = False
            
            
    #----- SOBREESCRITURA DE METODOS ------#

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        if self.sale_channel_id:
            invoice_vals['sale_channel_id'] = self.sale_channel_id.id
            invoice_vals['journal_id'] = self.sale_channel_id.invoice_journal_id.id
        return invoice_vals