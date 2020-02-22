from rest_framework import serializers

from .models import Showtime
from .models import Channel
from .models import Program


class ShowtimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Showtime
        fields = ('start_time', 'end_time', 'program')

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'  # fields = ('uid', 'original_title', 'local_title', 'year', 'channel')

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('uid', 'name', 'country_code')
