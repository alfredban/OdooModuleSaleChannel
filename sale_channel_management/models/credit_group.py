from odoo import models, fields, api

class CreditGroup(models.Model):
    _name = "credit.group"
    _description = "Grupos de créditos"

    #---------------------------------------------ATRIBUTOS----------------------------------------------------

    name = fields.Char(string = "Name", required = True)
    code = fields.Char(string = "Code", required = True)

    sale_channel_id = fields.Many2one(comodel_name = "sale.channel", string="Sale Channel", required = True)

    global_credit = fields.Monetary(string = "Global Credit", required = True)

    #---------------------------------------------CAMPOS COMPUTADOS----------------------------------------------------

    used_credit = fields.Monetary(compute = "_compute_used_credit", store=False)

    available_credit = fields.Monetary(string="Available credit", compute="_compute_available_credit", store=False)

    
    #---------------------------------------------RELACIONES----------------------------------------------------

    currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
        store=True,
        readonly=True
    )

    company_id = fields.Many2one(
        'res.company',
        default=lambda self: self.env.company.id,
        required=True
    )

    #---------------------------------------------CONSTRAINTS----------------------------------------------------

    _sql_constraints = [

        (
            'credit_group_code_unique',
            'unique(code)',
            'El código del grupo de crédito debe ser único.'
        )

    ]


    # ------------------------------
    # Cálculo del crédito utilizado
    # ------------------------------
    def _compute_used_credit(self):
        for group in self:
            total = 0
            company_currency = group.company_id.currency_id

            partners = self.env['res.partner'].search([
                ('credit_group_id', '=', group.id)
            ])

            # Ventas confirmadas sin facturar
            sale_orders = self.env['sale.order'].search([
                ('partner_id', 'in', partners.ids),
                ('state', '=', 'sale'),
                ('invoice_status', 'in', ['to invoice', 'no']),
            ])

            for so in sale_orders:
                total += so.currency_id._convert(
                    so.amount_total,
                    company_currency,
                    so.company_id,
                    fields.Date.today()
                )

            # Facturas impagas
            invoices = self.env['account.move'].search([
                ('partner_id', 'in', partners.ids),
                ('state', '=', 'posted'),
                ('payment_state', 'not in', ['paid'])
            ])

            for inv in invoices:
                total += inv.currency_id._convert(
                    inv.amount_total,
                    company_currency,
                    inv.company_id,
                    fields.Date.today()
                )

            group.used_credit = total

    @api.depends('global_credit', 'used_credit')
    def _compute_available_credit(self):
        for group in self:
            group.available_credit = group.global_credit - group.used_credit
