# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    student_id = fields.Many2one("student.information", string="Student")

