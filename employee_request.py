from odoo import api,fields,models,_,tools

class RequestEmployee(models.Model):
    _name = "employee.request"
    _description = "Employee Request"

    name = fields.Char(string="Employee Name")
    image = fields.Binary(string="Image", store=True, attachment=False)
    date_start = fields.Datetime()
    date_end = fields.Datetime()
    location = fields.Char(string="Location")
    contact = fields.Char(string="Contact")
    amount = fields.Integer(string="Amount")
    # request_category_id = fields.Many2one("request_category")
    # def create_new_request(self):
    #     print("new request created")

    def submit_details(self):
        return {
            'type': 'ir.actions.act_window',
            'target': 'current',
            'name': 'Submit',
            'view_mode': 'list',
            'res_model': 'employee.request'
        }
