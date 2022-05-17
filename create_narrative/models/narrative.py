# -*- coding: utf-8 -*-

from odoo import fields, models


class NarrativeTag(models.Model):
    _name = 'narrative.act.tag'
    _description = 'Marcadores de actos'

    name = fields.Char('Nombre')
    code = fields.Char('Código')


class NarrativeActType(models.Model):
    _name = 'narrative.act.type'
    _description = 'Tipo de actos'

    code = fields.Char(string='Código')
    sequence = fields.Integer(string='Secuencia')
    name = fields.Char(string='Nombre de tipo')


class NarrativePlace(models.Model):
    _name = 'narrative.scene.place'
    _description = 'Ubicaciones de escenas'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre de lugar')
    description = fields.Char(string='Descripción')


class NarrativePartnerType(models.Model):
    _name = 'narrative.partner.type'
    _description = 'Tipos de personajes'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre del tipo')
    description = fields.Char(string='Descripción')


class NarrativePartnerArc(models.Model):
    _name = 'narrative.partner.arc'
    _description = 'Arcos de personajes'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre del tipo')
    description = fields.Char(string='Descripción')


class NarrativePartnerDimension(models.Model):
    _name = 'narrative.partner.dimension'
    _description = 'Dimensiones del personaje'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre de dimensión')
    description = fields.Char(string='Descripción de la dimensión')


class NarrativePartnerFunction(models.Model):
    _name = 'narrative.partner.function'
    _description = 'Funciones del personaje'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre de función')
    description = fields.Char(string='Descripción de la función')
