from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    description='Generate ".xlsx" reports of programs aired between start_date and end_date.\n'
    'Optionally filter between start_time and end_time/n'
    '/nExample: vericast-reports -F my_report -Di 2018-02-26 -Df 2018-02-28 -Ti 12:00:30 -Tf 00:00:00/n'
    'Returns a file named "my_report.xslx" in the current directory, with the programs aired between ' 
    '"2018-02-26 12:00:30" and "2018-02-28 00:00:00"'

    
    help = 'Search for progrmas by date and save them in .xslx file.'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', 
            metavar='F', 
            type=str,
            help='Name of the ".xslx" file.'
            )
        parser.add_argument(
            'start_date', 
            metavar='Di', 
            type=str,
            help='Start date formatted as: "YYYY-MM-DD"'
            )
        parser.add_argument(
            'end_date', 
            metavar='Df', 
            type=str,
            help='End date formatted as: "YYYY-MM-DD"'
            )
        parser.add_argument(
            'start_time', 
            metavar='Ti', 
            type=str,
            default='00:00:00',
            help='Start time formatted as: "HH:MM"'
            )
        parser.add_argument(
            'end_time', 
            metavar='Tf', 
            type=str,
            default='00:00:00',
            help='End time formatted as: "HH:MM"'
            )


    def handle(self, *args, **kwargs):
        print(kwargs)
        # do something with the db and models views etc
