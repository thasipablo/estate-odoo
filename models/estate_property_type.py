from odoo import fields, models


class EstatePropertyModel(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Type'

    name = fields.Char()