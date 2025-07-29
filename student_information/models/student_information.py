from odoo import models,fields

class StudentInfo(models.Model):
    _name = 'student.information'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    entroll_no = fields.Integer(string='Entrollment No')
    education_info_ids = fields.One2many('education.info','student_id')
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)


