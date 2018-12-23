# -*- coding: utf-8 -*-
from django import template
# from django.contrib.sites.models import Site

register = template.Library()

@register.simple_tag
def current_domain():
    return 'http://localhost:8000'
    # return 'http://%s' % Site.objects.get_current().domain

@register.simple_tag
def github_url():
    return 'http://github.com/ThePocket006/register'