from odoo import models, fields


class EducationInfo(models.Model):
    _name = 'education.info'
    _description = 'Education Info'

    name = fields.Char(string='Name', required=True)
    percentage = fields.Float(string='Percentage')
    place = fields.Char(string='Place')
    student_id = fields.Many2one('student.information', string='Student')
    tag_ids = fields.Many2many('education.info.tag','education_id','tag_id')

class EducationInfoTag(models.Model):
    _name = 'education.info.tag'
    _description = 'Education Info tag'

    name = fields.Char(string='Name', required=True)

