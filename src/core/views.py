# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect


# Main TV AV html index
def home_view(request):
    return render(request, template_name='core/index.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('%s?next=%s' % ('', request.path))