from odoo import api, models, fields

class DocumentReportWizard(models.TransientModel):
    _name = "document.report.wizard"
    _description = 'Document Wizard'

    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')
    responsible_employee = fields.Many2one('res.users', string='Responsible Employee')

    def document_report(self):
        domain = []
        if self.date_from:
            domain.append(('create_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('create_date', '<=', self.date_to))
        if self.responsible_employee:
            domain.append(('responsible_employees', '=', self.responsible_employee.id))

        documents = self.env['document.management.document'].search(domain)
        print('Documents:', documents)
        #print('Clicked')
        #return True
