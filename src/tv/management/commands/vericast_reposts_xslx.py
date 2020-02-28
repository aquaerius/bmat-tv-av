import os
import pandas as pd
import numpy as np
import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from tv import models as tv_models

class VericastMatchReport:
    matches = []
    channel = None
    df = None

    def __init__(self, filename):
        self.df = pd.read_json(filename.split('-')[1])

    def model_data_for_xslx(self):


        df['title'] = df['title'].astype(str)
        df['start_time_utc'] = pd.to_datetime(yearfirst=True, utc=True)
        df['start_date'] = (df['start_time_utc'].astype(str)).map(
            lambda x: datetime.datetime.strptime(x, '%Y%m%dT%')
        )
        df['start_time'] = (df['start_time_utc'].astype(str)).map(
            lambda x: datetime.datetime.strptime(x, '%Y%m%dT%')
        )
        df['duration_in_seconds'] = pd.to_timedelta(df['duration_in_seconds'], unit='seconds')
        df['end_time'] = df['start_time'] + df['duration_in_seconds']
        df = df.drop(['start_date', 'duration_in_seconds'], axis=1)
        self.df = df
        logger.info('Dataframe modeled for database upload.')
        print('Dataframe modeled for database upload.')

    def create_channel(self,row):
        channel, created = tv_models.Channel.objects.get_or_create(
            uid=row.channel_id,
            name=row.channel_name,
            country_code=row.channel_country
            )
        if created:
            channel.save()
            self.channels.append(channel)
            logger.info('Channel {} from {} with id {} added to DB.'.format(
                channel.name,
                channel.country_code,
                channel.id
                ))
            print('Channel {} from {} with id {} added to DB.'.format(
                channel.name,
                channel.country_code,
                channel.id
                ))
        return channel

    def create_program(self,row, channel):
        if row.program_year != 'n/a':
            year = row.program_year[0:4]
        else:
            year = row.program_year
        program, created =tv_models.Program.objects.get_or_create(
            uid=row.program_id, 
            channel=channel,
            year=year,
            local_title=row.program_local_title,
            original_title=row.program_original_title
            )
        if created:
            program.save()
            self.programs.append(program)
            logger.info("Program {} with id {} added to DB.".format(
                program.local_title,
                program.uid,
                ))
            print("Program {} with id {} added to DB.".format(
                program.local_title,
                program.uid,
                ))
        return program

    def create_showtime(self,row, program):
        showtime, created = tv_models.Showtime.objects.get_or_create(
            program=program,
            start_time=row.start_time,
            end_time=row.end_time
            )
        if created:
            showtime.save()
            self.showtimes.append(showtime)
            logger.info('Showtime starting on {} added to '.format(row.start_time)+program.local_title)
            print('Showtime starting on {} added to '.format(row.start_time)+program.local_title)
        return showtime
    
    @classmethod
    def upload_showtimes(cls, self):
        for index, row in self.df.iterrows():
            channel = cls.create_channel(self, row)
            program = cls.create_program(self, row, channel)
            cls.create_showtime(self, row, program)
        return


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
        # verify file exists
        # make it a valid JSON
        # Load into df
        # Filter by kwargs
        # output to xslx
        # lines in file are: {"title": "Something Is Coming", "length": 3, "album": "Crime Drama", "artist": "Robert J Walsh", "start_time_utc": "2018-02-16T06:34:01.000000"}
        # Make JSON valid or loop through each line in file and add to df
        
        with open
        df = pd.DataFrame
        df.app
        # Make start_time_utc
        start_time_utc = datetime.datetime.strptime(kwargs['start_date']+kwargs['start_time'], '%Y-%m-%d%H:%M')
        end_time = datetime.datetime.strptime(kwargs['end_date']+kwargs['end_time'], '%Y-%m-%d%H:%M')
        programs = tv_models.Showtime.objects.filter(start_time__gt=start_time, start_time__lt=start_time)
        print(programs)





