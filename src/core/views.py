# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Main TV AV html index
def home(request):
    return render(request, template_name='core/index.html')
