from odoo import fields, models


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[
        ('new','New'), 
        ('offer received','Offer Received'),
        ('offer accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled')
    ], required=True, copy=False, default='new')

    name = fields.Char(required=True, string="Title")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area(msq)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[
        ('east','East'),
        ('west', 'West'),
        ('north','North'),
        ('south', 'South')
    ])

    property_type_id = fields.Many2one(comodel_name='estate.property.type', string='Estate Property Type')
    property_tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    salesperson_id = fields.Many2one(comodel_name='res.users', string='Sales Person', default=lambda self: self.env.user)
    buyer_id = fields.Many2one(comodel_name='res.partner', string='Buyer Person')
    offer_ids = fields.One2many('estate.property.offer','property_id', string='Offers')
    