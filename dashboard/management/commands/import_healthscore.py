import time
from dashboard.models import *
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import csv

import pytz


class Command(BaseCommand):
	def handle(self, *args, **options):
		first_row = True
		for row in csv.reader(open('output.csv')):
			if not first_row:
				print row[0]
				HealthscoreFactor, found = HealthscoreFactors.objects.update_or_create(systemId=row[0], defaults = {
					'healthscore':row[1],'capacity_total_freePct':row[2],'delAcksPct':row[3],'portReadBandwidthMBPS':row[4],
								'portWriteBandwidthMBPS':row[5], 'cpuLatestTotalAvgPct':row[6], 'cpuLatestTotalMaxPct':row[7],
								'nodeCountMissing':row[9],'ddsSizeUsedTiB':row[10]
									})
			else:
				first_row = False
