# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from views import ChannelDetailView
from views import ChannelListView
from views import ProgramDetailView
from views import ProgramListView
from views import ShowtimeDetailView
from views import showtimes_view

from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include

app_name = 'tv'

urlpatterns = [
    url(r'^programs/$', login_required(ProgramListView.as_view()), name='programs'),
    url(r'^programs/(?P<pk>\d+)/$', login_required(ProgramDetailView.as_view()), name='program-detail'),
    url(r'^programs/showtime/(?P<pk>\d+)/$', login_required(ShowtimeDetailView.as_view()), name='showtime-detail'),
    url(r'^showtimes/$', login_required(showtimes_view), name='showtimes'),
    url(r'^channels/$', login_required(ChannelListView.as_view()), name='channels'),
    url(r'^channels/(?P<pk>\d+)/$', login_required(ChannelDetailView.as_view()), name='channel-detail'),
]
