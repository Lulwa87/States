#!/usr/bin/env python

import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import State, StateCapital

import django
django.setup()
# State.objects.all().delete()

dir_path = os.path.dirname(os.path.abspath(__file__))

states_csv = os.path.join(dir_path, 'states.csv')

csv_file = open(states_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	# print row['state']
	# print row['abbrev']
	# print row['capital']
	# print row['longitude']
	# print row['latitude']
	# print row['population']

	# new_state = State()
	new_state, created = State.objects.get_or_create(name=row['state'])
	new_state.abbreviation = row['abbrev']
	new_state.save()

	new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
	new_capital.state = new_state
	new_capital.latitude = row['latitude']
	new_capital.longitude = row['longitude']
	new_capital.capital_population = row['population']

	try:
		new_capital.save()
	except Exception, e:
		print new_capital.name
		print e 


