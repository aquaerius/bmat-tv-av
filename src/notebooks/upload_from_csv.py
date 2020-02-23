import os
import sys

import pandas as pd
import numpy as np
import datetime

from django.db import IntegrityError

from tv import models as tv_models


# Change DataFrame dtypes to match Database models
def model_for_db(csv):
    """
    @parameters:
    - csv: Electronic Guide filename in comma separated values (.csv)

    @returns:
    - Dataframe with items formatted for bmat tv/av programs
    """

    # Load csv into Dataframe
    df = pd.read_csv(csv)

    # Fill n/a with readable string "n/a"
    df = df.fillna('n/a')
    df['program_year'] = df['program_year'].astype(str)
    df['start_time'] = (df['start_date'].astype(str) + ' ' + df['start_time']).map(
        lambda x: datetime.datetime.strptime(x, '%Y%m%d %H:%M')
    )
    df['duration_in_seconds'] = pd.to_timedelta(df['duration_in_seconds'], unit='seconds')
    df['end_time'] = df['start_time'] + df['duration_in_seconds']
    df = df.drop(['start_date', 'duration_in_seconds'], axis=1)
    return df


# Get or create Program with channel obj and row data
def create_program(row, channel):
    if row.program_year != 'n/a':
        year = row.program_year[0:4]
    else:
        year = row.program_year
    program, created =tv_models.Program.objects.get_or_create(uid=row.program_id, channel=channel,
                                                            year=year,
                                                            local_title=row.program_local_title,
                                                            original_title=row.program_original_title
                                                            )
    if created:
        program.save()
        print("Program {} with id {} added to DB.".format(program.local_title,
                                                          program.uid,
                                                          ))
    return program


def create_channel(row):
    channel, created = tv_models.Channel.objects.get_or_create(uid=row.channel_id,
                                                     name=row.channel_name,
                                                     country_code=row.channel_country
                                                     )
    if created:
        channel.save()
        print('Channel {} from {} with id {} added to DB.'.format(channel.name,
                                                                  channel.country_code,
                                                                  channel.id
                                                                  ))
    return channel


def create_showtime(row, program):
    showtime, created = tv_models.Showtime.objects.get_or_create(program=program,
                                                              start_time=row.start_time,
                                                              end_time=row.end_time
                                                              )
    if created:
        showtime.save()
        print('Showtime starting on {} added to {}.'.format(row.start_time,
                                                            program
                                                            ))
    return showtime


# Create Showtimes from DataFrame
def add_showtimes_from_dataframe(df, filename):
    for index, row in df.iterrows():
        channel = create_channel(row)
        program = create_program(row, channel)
        create_showtime(row, program)

    print("Finished adding programs from {}".format(filename))


def main():
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

    if len(sys.argv) == 1:
        filename = None
        while filename is None:
            filename = input('Please enter the full path to the Electronic Program Guide: ')
            if os.path.isfile(filename):
                os.chdir(filename[0:-len(filename.split('/')[-1])])
                print ("Uploading programs to database...")
                df = model_for_db(filename.split('/')[-1])
                add_showtimes_from_dataframe(df, filename)
                print ("Finished uploading programs from {} to database.".format(filename))
            else:
                filename = None
                print ("File does not exist")
    elif len(sys.argv) > 1:
        filename = None
        filenames = sys.argv[1:]
        while filename is None:
            if os.path.isfile(any(filenames.__iter__())) is False:
                print ("File {} does not exist".format(filename))
                filename = None
            else:
                for filename in filenames:
                    print ("Uploading programs to database...")
                    df = model_for_db(filename)
                    add_showtimes_from_dataframe(df, filename)


if "__name__" == "__main__":
    main()
