# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Vista principal, no requiere login
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

# Vista para otras páginas
def pages(request):
    context = {}
    # Todas las rutas de recursos terminan en .html.
    # Obtiene el nombre del archivo html desde la url y carga ese template.
    try:

        load_template = request.path.split('/')[-1]

        # Si la ruta es 'admin', redirige al panel de administración de Django
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        context['segment'] = load_template

        # Intenta cargar el template correspondiente
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        # Si no existe el template, carga la página 404
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        # En caso de otros errores, carga la página 500
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
