from odoo import models, fields

class InheritHrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    father_name = fields.Char(string="Father Name")
    grandfather_name = fields.Char(string="Grandfather Name")
