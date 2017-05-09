import time
from dashboard.models import *
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import csv

import pytz


class Command(BaseCommand):
	def handle(self, *args, **options):
		hs = HealthscoreFactors.objects.all()

		for score in hs:
			print score
			server = Server.objects.get(serialNumberInserv=score.systemId)
			server.healthscore = score
			server.save()
			print score.systemId
