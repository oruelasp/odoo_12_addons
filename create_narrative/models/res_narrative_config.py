# -*- coding: utf-8 -*-

from odoo import fields, models


class ResNarrativeConfig(models.Model):
    _name = 'res.narrative.config'
    _description = 'Plantilla de Eje'

    code = fields.Char(string='Código')
    name = fields.Char(string='Título', help='Título de la plantilla para libro/guión/película')
    act_ids = fields.One2many('res.narrative.config.line', 'config_id', string='Actos de narrativa')


class ResNarrativeConfigLine(models.Model):
    _name = 'res.narrative.config.line'
    _description = 'Detalle de Plantilla'

    config_id = fields.Many2one('res.narrative.config', string='Configuración de Narrativa')
    name = fields.Char(string='Nombre de acto')
    type = fields.Many2one('narrative.act.type', string='Tipo de acto')
    tag_ids = fields.Many2many('narrative.act.tag', 'config_line_tag_rel', 'config_line_id', 'tag_id', string='Marcadores')


