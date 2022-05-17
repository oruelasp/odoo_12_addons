# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer('Edad')
    children_ids = fields.Many2many('res.partner', 'partner_family_rel', 'parent_id', 'child_id', 'Hijos')
    parents_ids = fields.Many2many('res.partner', 'partner_family_rel', 'child_id', 'parent_id', 'Padres')
    is_character = fields.Boolean('¿Es personaje narrativo?')
    narrative_principal_ids = fields.Many2many('res.narrative', 'narrative_partner_principal_rel', 'partner_id', 'narrative_id',
                                             string='Narrativa de personajes principales')
    narrative_secondary_ids = fields.Many2many('res.narrative', 'narrative_partner_secondary_rel', 'partner_id', 'narrative_id',
                                             string='Narrativa de personajes secundarios')

    @api.multi
    def name_get(self):
        res = []
        for record in self:
            if record.parent_id:
                name = '{} ({})'.format(record.name, record.age)
            else:
                name = '{}'.format(record.name)
            res.append((record.id, name))
        return res
