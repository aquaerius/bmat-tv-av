# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from tv.models import Channel, Program, Showtime

admin.site.register(Channel)
admin.site.register(Program)
admin.site.register(Showtime)
