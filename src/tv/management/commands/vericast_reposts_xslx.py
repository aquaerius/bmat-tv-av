import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from tv import models as tv_models

class Command(BaseCommand):
    description='Generate ".xlsx" reports of programs aired between start_date and end_date.\n'
    'Optionally filter between start_time and end_time/n'
    '/nExample: vericast-reports -F my_report -Di 2018-02-26 -Df 2018-02-28 -Ti 12:00:30 -Tf 00:00:00/n'
    'Returns a file named "my_report.xslx" in the current directory, with the programs aired between ' 
    '"2018-02-26 12:00:30" and "2018-02-28 00:00:00"'

    
    help = 'Search for progrmas by date and save them in .xslx file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file-path', 
            type=str,
            help='Name of the ".xslx" file.'
            )
        parser.add_argument(
            '--start-date', 
            type=str,
            help='Start date formatted as: "YYYY-MM-DD"'
            )
        parser.add_argument(
            '--start-time', 
            type=str,
            default='00:00:00',
            help='Start time formatted as: "HH:MM"'
            )
        parser.add_argument(
            '--end-date', 
            type=str,
            help='End date formatted as: "YYYY-MM-DD"'
            )
        parser.add_argument(
            '--end-time', 
            type=str,
            default='00:00:00',
            help='End time formatted as: "HH:MM"'
            )


    def handle(self, *args, **kwargs):
        start_time = datetime.datetime.strptime(kwargs['start_date']+kwargs['start_time'], '%Y-%m-%d%H:%M')
        end_time = datetime.datetime.strptime(kwargs['end_date']+kwargs['end_time'], '%Y-%m-%d%H:%M')
        programs = tv_models.Showtime.objects.filter(start_time__gt=start_time, end_time__lt=end_time)
        print(programs)