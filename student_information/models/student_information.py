from odoo import models,fields, api
from datetime import date

class StudentInfo(models.Model):
    _name = 'student.information'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    entroll_no = fields.Integer(string='Entrollment No')
    education_info_ids = fields.One2many(comodel_name='education.info',inverse_name='student_id')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', required=True)
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string='Age', compute='_compute_age')
    last_name = fields.Char(string='Last Name')
    full_name = fields.Char(string='Full Name', compute='_compute_full_name',
                            inverse='_inverse_full_name', store=True)
    category = fields.Selection(selection=[
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('graduate', 'Graduate')
    ], string='Category', default='junior')
    category_note = fields.Text(string='Category Note')
    email = fields.Char(related="partner_id.email", string="Email")

    @api.depends('birth_date')
    def _compute_age(self):
        """
        Compute the age of the record based on the birth_date field.

        The age is calculated as the difference in years between today's date
        and the birth_date, adjusting for whether the birthday has occurred
        yet this year. If no birth_date is set, the age will be set to 0.
        :return: None
        """
        for record in self:
            if record.birth_date:
                today = date.today()
                birth_date = fields.Date.from_string(record.birth_date)
                age = today.year - birth_date.year
                if today.month < birth_date.month or (
                        today.month == birth_date.month and today.day < birth_date.day):
                    age -= 1
                record.age = age
            else:
                record.age = 0

    @api.depends('name', 'last_name')
    def _compute_full_name(self):
        """
        Compute the full name of the record by combining the name and last_name fields.

        - If both 'name' and 'last_name' are set, 'full_name' will be a combination of both.
        - If only 'name' is set, 'full_name' will be equal to 'name'.
        - If 'name' is not set, 'full_name' will be set to False.
        :return: None
        """
        for record in self:
            if record.name and record.last_name:
                record.full_name = f"{record.name} {record.last_name}"
            elif record.name:
                record.full_name = record.name
            else:
                record.full_name = False

    def _inverse_full_name(self):
        """
        Inverse method for the 'full_name' computed field.

        Splits the 'full_name' into 'name' and 'last_name':
        - If 'full_name' contains a space, the first part is assigned to 'name'
          and the second part to 'last_name'.
        - If 'full_name' contains only one word, it is assigned to 'name'
          and 'last_name' is set to False.
        - If 'full_name' is not set, both 'name' and 'last_name' are set to False.
        :return: None
        """
        for record in self:
            if record.full_name:
                parts = record.full_name.split(' ', 1)
                record.name = parts[0]
                record.last_name = parts[1] if len(parts) > 1 else False
            else:
                record.name = False
                record.last_name = False

    @api.onchange('category')
    def _onchange_category(self):
        """
        Updates the 'category_note' field based on the selected 'category'.

        - 'junior': Sets note indicating the student requires basic courses.
        - 'senior': Sets note indicating eligibility for advanced courses.
        - 'graduate': Sets note indicating eligibility for postgraduate programs.
        - Any other or empty value: Clears the note.
        :return: None
        """
        if self.category:
            if self.category == 'junior':
                self.category_note = "Student is in junior level, requires basic courses."
            elif self.category == 'senior':
                self.category_note = "Student is in senior level, eligible for advanced courses."
            elif self.category == 'graduate':
                self.category_note = "Student is a graduate, eligible for postgraduate programs."
            else:
                self.category_note = False
        else:
            self.category_note = False