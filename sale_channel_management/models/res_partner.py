from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_group_id = fields.Many2one("credit.group", string="Grupo de Crédito")
