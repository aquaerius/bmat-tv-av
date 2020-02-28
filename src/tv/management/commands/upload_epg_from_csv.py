import os
import sys
import pandas as pd
import numpy as np
import datetime
import logging


from django.db import IntegrityError
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from tv import models as tv_models

# For compatibility withother Django versions and using shell_plus --notebook
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Get an instance of a logger
logger = logging.getLogger(__name__)

class ProgramGuideUpload:
    channels = []
    programs = []
    showtimes = []
    df = None

    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def model_data_for_db(self):
        df = self.df.fillna('n/a')
        df['program_year'] = df['program_year'].astype(str)
        df['start_time'] = (df['start_date'].astype(str) + ' ' + df['start_time']).map(
            lambda x: datetime.datetime.strptime(x, '%Y%m%d %H:%M')
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
    
    help = 'Upload Electronic TV program guides to database in comma separated values (.csv)'
    
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='The full path to the csv file.')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        try:
            if os.path.isfile(filename):
                os.chdir(filename[0:-len(filename.split('/')[-1])])
                filename = filename.split('/')[-1]
                print ("Starting upload of EPG TV programs to database...")
                
                upload = ProgramGuideUpload(filename)
                upload.model_data_for_db()
                ProgramGuideUpload.upload_showtimes(upload)
                print("Finished uploading programs from {} to database.".format(filename))

        except Exception as e:
            print(e)
            