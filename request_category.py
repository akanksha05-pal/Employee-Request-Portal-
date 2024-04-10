from odoo import api,fields,models,_,tools

class RequestCategory(models.Model):
    _name = "request.category"
    _description = "Request Category"

    name = fields.Char(string="Request Type")
    image = fields.Binary(string="Image", store=True, attachment=False)
    # date_start = fields.Datetime()
    # date_end = fields.Datetime()
    # location = fields.Char(string="Location")
    # contact = fields.Char(string="Contact")
    # amount = fields.Integer(string="Amount")
    # employee_request_ids = fields.One2many(co_model="employee_request",reverse="request_category_id",string="")


    # def create_new_request(self):
    #     print("new request created")

    # def confirm_details(self):
    #     print("submit details")


    def new_request_func(self):
        return {
            'type': 'ir.actions.act_window',
            'target': 'current',
            'name': 'Employee Request',
            'view_mode': 'form',
            'res_model': 'employee.request',
        }
