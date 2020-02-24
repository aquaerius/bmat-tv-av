# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from rest_framework import serializers

from .models import Showtime
from .models import Channel
from .models import Program
from .models import COUNTRY_CHOICES


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    uid = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100, read_only=True)
    country = serializers.SerializerMethodField()

    def get_country(self, obj):
        channel = obj
        country = channel.get_country_code_display()
        return country

    class Meta:
        model = Channel
        fields = ('url', 'uid', 'name', 'country')

class ProgramSerializer(serializers.ModelModelSerializer):
    channel = ChannelSerializer()
    
    class Meta:
        model = Program
        fields = ('uid', 'original_title', 'local_title', 'year', 'channel')


class ShowtimeSerializer(serializers.HyperlinkedModelSerializer):
    program = ProgramSerializer()
    start_time = serializers.DateTimeField(read_only=True, format="%H:%M")
    start_date = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    

    def get_start_date(self, obj):
        start_time = obj.start_time
        start_date = datetime.datetime.strftime(start_time, '%Y-%m-%d')
        # Convert to date only format
        return start_date

    def get_duration(self, obj):
        showtime  = obj
        duration = datetime.timedelta.total_seconds(showtime.end_time - showtime.start_time)
        # Convert to date only format
        return duration


    class Meta:
        model = Showtime
        fields = ('url', 'program', 'start_date', 'start_time', 'duration' )
