from odoo import models, fields

class Document(models.Model):
    _name = 'document.management.document'
    _description = 'Document Management'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    company = fields.Many2one('res.company', string='Company')
    creator_user = fields.Many2one('res.users', string='Created by', default=lambda self: self.env.user)
    responsible_employees = fields.Many2many('hr.employee', string='Responsible Employees')
    create_date = fields.Datetime(string='Date', default=fields.Datetime.now)

    def open_document_report(self):
        return {'type': 'ir.actions.act_window',
                'res_model': 'document.report.wizard',
                'view_mode': 'form',
                'view_id': False,
                'target': 'new',
        }