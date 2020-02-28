import datetime
import json
import os

import dateutil.parser
import numpy as np
import pandas as pd
from django.core.management.base import BaseCommand
from django.utils.encoding import python_2_unicode_compatible

from tv import models as tv_models


@python_2_unicode_compatible
class VericastMatchReporter:
    """
    @params: filename, start_date, start_time, end_date, end_time, time_zone
    """
    filename = None
    channel = None
    report_name = 'vericast-api-matches'
    report_file_extension = 'xlsx'
    df = pd.DataFrame(columns=['title','length','album','artist','start_time_utc'])
    matches_between_dates = None
    start_time = None
    end_time = None
    dfeng = None
    
    
    def __init__(self, **kwargs):
        """Initilize report, make a pandas dataframe with the matches."""
        
        self.filename = kwargs['filename']
        self.channel = self.filename.split('/')[-1].split('-')[-1].split('.')[0]
        self.report_name += '-' + self.channel 
        try:
            # Make a df with engineer's times and bring them to UTC for correct comparison
            start_time_naive = dateutil.parser.parse(kwargs['start_date']+'T'+kwargs['start_time'])
            end_time_naive = dateutil.parser.parse(kwargs['end_date']+'T'+kwargs['end_time'])
            dfeng = pd.DataFrame({'naive_datetime':[start_time_naive,end_time_naive]}, index=['filter_start','filter_end'])
            dfeng['local_datetime'] = pd.DatetimeIndex(dfeng['naive_datetime']).tz_localize(tz =kwargs['time_zone'])
            dfeng['utc_datetime'] = pd.DatetimeIndex(dfeng['local_datetime']).tz_convert(tz ='UTC')
            self.dfeng = dfeng
            self.report_name +=' {} to {}'.format(self.dfeng.loc['filter_start']['local_datetime'],self.dfeng.loc['filter_end']['local_datetime'])
            self.report_name =kwargs['destination_dir']+'/'+self.report_name + '.{}'.format(self.report_file_extension)
        except:
            raise
        with open(self.filename) as f:
            for line in f.readlines():
                # Append line into df
                self.df = self.df.append(json.loads(line), ignore_index=True)
                
        # Cast dates as aware datetime with timezone 'UTC'
        self.df['start_time_utc'] = pd.to_datetime(self.df['start_time_utc'], yearfirst=True, utc=True)
        print('Reporter initialized.')
        
    def create_report_between_times_xlsx(self):
        print("Finding programs that match from channel: {}".format(self.channel))        
        # Make a mask boolean mask between dates
        mask = (self.df['start_time_utc'] >= self.dfeng.loc['filter_start']['utc_datetime']) & (self.df['start_time_utc'] <= self.dfeng.loc['filter_end']['utc_datetime'])
        self.matches_between_dates = self.df.loc[mask]
        # Write report to xslx
        writer = pd.ExcelWriter(self.report_name, engine='openpyxl')
        self.matches_between_dates.to_excel(writer, sheet_name=self.channel, index=False)
        writer.save()
        writer.close()
        print('File {} with {} matches has been created'.format(str(self.report_name), len(self.matches_between_dates.length)).decode('utf-8'))
    
    def __str__(self):
        return 'Vericast API matches from '+self.channel.replace('_', ' ').upper()+' between times '+str(self.start_time)+' and '+str(self.end_time)+' UTC'

    def __repr__(self):
        return "<{}: Channel {}>".format(self.__class__.__name__, self.channel)
    

class Command(BaseCommand):
    # TODO Chenge description filename
    description='Generate ".xlsx" reports of programs aired between start_date and end_date.\n'
    'Optionally filter between start_time and end_time, and timezone./n'
    '/nExample: vericast-reports --filename matches-my_channel.json --start-date 2018-02-26 --end-date 2018-02-28 --start-time 12:00 --end-time 00:00:'
    '--time-zone "Europe/Madrid" \n Returns a file named "vericast-matches-report-channel-startdate-to-end-date.xslx" in the current directory, with the programs aired between ' 
    '"2018-02-26 12:00" and "2018-02-28 00:00".'

    
    help = 'Search for programs by date and save them in .xlsx file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--filename', 
            type=str,
            required=True,
            help='Name of the ".json" file.'
            )
        parser.add_argument(
            '--start-date', 
            type=str,
            help='Start date formatted as: "YYYY-MM-DD"'
            )
        parser.add_argument(
            '--start-time', 
            type=str,
            default='00:00',
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
            default='00:00',
            help='End time formatted as: "HH:MM"'
            )
        parser.add_argument(
            '--time-zone', 
            type=str,
            help='Time zone offset from UTC time. (Example: Enter "Europe/Madrid")',
            default="UTC"
            )
            
    def handle(self, *args, **kwargs):
        # Verify file exists
        try:
            if os.path.isfile(kwargs['filename']):
                # Store destination directory
                kwargs['destination_dir'] = os.getcwd()
                # Change working directory
                os.chdir(kwargs['filename'][0:-len(kwargs['filename'].split('/')[-1])])
                kwargs['filename'] = kwargs['filename'].split('/')[-1]
                 # Create reporter from file
                reporter = VericastMatchReporter(**kwargs)
                reporter.create_report_between_times_xlsx()
        except Exception as e:
            print(e)
