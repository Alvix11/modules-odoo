from odoo import models, fields # type: ignore

class StateProperty(models.Model):
    _name = 'state.property'
    _description = 'State Property'

    name = fields.Char()
