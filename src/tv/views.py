# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils import timezone
import datetime
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .models import Channel
from .models import Program
from .models import Showtime
from .serializers import ChannelSerializer
from .serializers import ProgramSerializer
from .serializers import ShowtimeSerializer
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


from .forms import ProgramForm
from django.views.generic.edit import FormView


def showtimes_view(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProgramForm(request.POST,initial={'max_number': '3'})
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            local_title = request.POST.get('local_title','')
            country_code = request.POST.get('country_code','N/A')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            start_time = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_time = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            context = {}
            context['showtimes'] = Showtime.objects.filter(
                start_time__gt=start_time, 
                end_time__lt=end_time)
            if local_title != '':
                # decode title
                context['showtimes'] = context['showtimes'].filter(program__local_title__iexact=local_title)
            if country_code != 'N/A':
                context['showtimes'] = context['showtimes'].filter(program__channel__country_code=country_code)
            context['showtimes'] = context['showtimes'].order_by(
                'program__local_title','program__id','-start_time'
                )
            return render(request, "tv/showtime_list.html", context)
        else:
            messages.error(request, 'The form is invalid.')
            return HttpResponseRedirect('')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProgramForm()
        return render(request, "tv/program_search.html", {'form':form})


# Create your views here.
def home_view(request):
    return render(request, template_name='tv/index.html')


class ChannelListView(ListView):

    model = Channel
    paginate_by = 50  # if pagination is desired
    ordering = ['name','uid']

    def get_context_data(self, **kwargs):
        context = super(ChannelListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
          

class ChannelDetailView(DetailView):

    model = Channel
    paginate_by = 50  # if pagination is desired
    
    def get_context_data(self, **kwargs):
        context = super(ChannelDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['programs'] = context['object'].programs.order_by('local_title','-uid')
        return context


class ProgramListView(ListView):

    model = Program
    paginate_by = 50  # if pagination is desired
    ordering = ['local_title']

    def get_context_data(self, **kwargs):
        context = super(ProgramListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProgramDetailView(DetailView):

    model = Program
    paginate_by = 50  # if pagination is desired
    ordering = ['-start_time']

    def get_context_data(self, **kwargs):
        context = super(ProgramDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['showtimes'] = context['object'].showtimes.order_by('-start_time')
        return context


class ShowtimeDetailView(DetailView):

    model = Showtime

    def get_context_data(self, **kwargs):
        context = super(ShowtimeDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        showtime = context['object']
        context['duration'] = datetime.timedelta.total_seconds(showtime.end_time - showtime.start_time)
        return context


class ShowtimeViewSet(viewsets.HyperlinkedModelViewSet):
    """
    API endpoint that allows program times to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,) 
    queryset = Showtime.objects.all().order_by('program','-start_time')
    serializer_class = ShowtimeSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows channels to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,) 
    queryset = Channel.objects.all().order_by('uid','-name')
    serializer_class = ChannelSerializer
