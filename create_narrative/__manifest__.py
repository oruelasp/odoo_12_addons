# -*- coding: utf-8 -*-

{
    'name': 'Crear Estructura Narrativa',
    'version': '1.1.1',
    'category': 'Others',
    'license': 'Other proprietary',
    'summary': 'Este app permite crear una estructura literaria o cinematográfica',
    'description': """
Permite crear estructurar de narración o de cinematografía. Estructurar personajes, escenas y secuencias.
    """,
    'author': 'Omar Rodrigo Ruelas Principe',
    'depends': [
        'base'
    ],
    'data': [
        'views/res_narrative_views.xml',
        'views/res_partner_views.xml',
        'views/res_narrative_config_views.xml',
        'views/narrative_views.xml',
        'views/res_narrative_menus.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
