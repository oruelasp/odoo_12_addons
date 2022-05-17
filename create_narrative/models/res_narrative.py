# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResNarrative(models.Model):
    _name = 'res.narrative'
    _description = 'Eje Narrativo'

    name = fields.Char(string='Título', help='Título del libro/guión/película')
    synopsis = fields.Char(string='Sinopsis')
    plot = fields.Char(string='Argumento')
    theme = fields.Char(string='Tema')
    config_id = fields.Many2one('res.narrative.config', string='Plantilla')
    partner_ids = fields.One2many('narrative.partner', 'narrative_id', string='Personajes')
    act_ids = fields.One2many('narrative.act', 'narrative_id', string='Actos/Secciones')

    @api.onchange('synopsis')
    def _onchange_synopsis(self):
        if self.synopsis:
            init_message = 'La historia consiste en lo siguiente: '
            self.plot = '''
                {init_message}{synopsis}
            '''.format(init_message=init_message, synopsis=self.synopsis)


class NarrativePartner(models.Model):
    _name = 'narrative.partner'
    _description = 'Personajes Narrativos'

    narrative_id = fields.Many2one('res.narrative', string='Eje narrativo')
    partner_id = fields.Many2one('res.partner', string='Personaje', help='Seleccionar versión si aplica')
    partner_type_id = fields.Many2one('narrative.partner.type', string='Tipo de personaje')
    partner_arc_id = fields.Many2one('narrative.partner.arc', string='Arco de personaje')
    partner_line_ids = fields.One2many('narrative.partner.line', 'narrative_partner_id', string='Tipo de personaje')
    partner_function_id = fields.Many2one('narrative.partner.function', string='Función del personaje')


class NarrativePartnerLine(models.Model):
    _name = 'narrative.partner.line'
    _description = 'Detalle de personajes'

    narrative_partner_id = fields.Many2one('narrative.partner', string='Personaje narrativo')
    dimension_id = fields.Many2one('narrative.partner.dimension', string='Dimensión del personaje')
    name = fields.Char(string='Descripción de dimensión')


class NarrativeAct(models.Model):
    _name = 'narrative.act'
    _description = 'Acto Narrativo'

    sequence = fields.Integer(string='Secuencia')
    narrative_id = fields.Many2one('res.narrative', string='Eje narrativa')
    name = fields.Char(string='Nombre de acto')
    type = fields.Many2one('narrative.act.type', string='Tipo de acto')
    tag_ids = fields.Many2many('narrative.act.tag', 'narrative_act_tag_rel', 'act_id', 'tag_id', string='Marcadores')
    chapter_ids = fields.One2many('narrative.chapter', 'act_id', string='Capítulos')


class NarrativeChapter(models.Model):
    _name = 'narrative.chapter'
    _description = 'Capítulo Narrativo'
    _order = 'sequence'

    sequence = fields.Integer(string='Secuencia')
    act_id = fields.Many2one('narrative.act', string='Acto narrativo')
    synopsis = fields.Char(string='Sinopsis')
    name = fields.Char(string='Nombre de capítulo')
    partner_ids = fields.Many2many('res.partner', 'chapter_partner_rel', 'chapter_id', 'partner_id', string='Personajes')
    tag_id = fields.Many2one('narrative.act.tag', string='Marcador')
    scene_ids = fields.One2many('narrative.scene', 'chapter_id', string='Escenas')


class NarrativeScene(models.Model):
    _name = 'narrative.scene'
    _description = 'Escena Narrativa'

    sequence = fields.Integer(string='Secuencia')
    chapter_id = fields.Many2one('narrative.chapter', string='Capítulo')
    place_id = fields.Many2one('narrative.scene.place', string='Ubicación')
    name = fields.Char(string='Nombre de escena')
    synopsis = fields.Char(string='Sinopsis')
    reference = fields.Char(string='Referencia')
    partner_ids = fields.Many2many('res.partner', 'scene_partner_rel', 'scene_id', 'partner_id', string='Personajes')
    event_ids = fields.One2many('narrative.event', 'scene_id', string='Eventos')


class NarrativeEvent(models.Model):
    _name = 'narrative.event'
    _description = 'Evento Narrativa'

    sequence = fields.Integer(string='Secuencia')
    scene_id = fields.Many2one('narrative.scene', string='Escenario')
    name = fields.Char(string='Nombre de escena')
    description = fields.Char(string='Descripción')
    relevant_context = fields.Char(string='Hecho Relevante')
    partner_id = fields.Many2one('res.partner', string='Personaje del evento')
