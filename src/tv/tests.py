# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase

from tv import models as tv_models


class ShowtimeTestCase(TestCase):

	def setUp(self):
		# Create a channel
		channel = tv_models.Channel(
			uid=99999999999,
			name='MTV',
			country_code='USA'
			)
		channel.save()

		# Create a program
		tv_models.Program(
			uid=123456789,
			original_title="Bang Bang Bang!",
			local_title = "Pum Pum Pum",
			year = 1984,
			channel=channel
			).save()

	def test_showtime_representation(self):
		program = tv_models.Program.objects.get(original_title='Bang Bang Bang!')
		print(str(program))
		start_time = '2018-02-13 10:20:00'
		showtime = tv_models.Showtime(program=program)
		showtime.save()
		showtime.start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
		self.assertEqual(str(showtime), 'Showtime on {} on {}'.format(start_time, program))


class ProgramTestCase(TestCase):
	def setUp(self):
    	# Create a channel
		tv_models.Channel(
			uid=99999999999,
			name='MTV',
			country_code='USA'
			).save()

	def test_create_program(self):
		channel = tv_models.Channel.objects.get(name='MTV')
		program = tv_models.Program(
			uid=123456789,
			original_title="Bang Bang Bang!",
			local_title = "Pum Pum Pum",
			year = 1984,
			channel=channel
			)
		program.save()
		program_2=tv_models.Program.objects.get(original_title='Bang Bang Bang!')
		self.assertEqual(program,program_2)
