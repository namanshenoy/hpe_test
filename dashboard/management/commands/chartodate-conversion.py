import time
from dashboard.models import *
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import pytz


class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in ServerRecord.objects.all():
            print type(obj.fromDate)
            print obj.fromDate.encode('ascii')
            try:
                obj.fromDateField = pytz.utc.localize(datetime.strptime(obj.fromDate.decode('ascii'), '%Y-%m-%d %H:%M:%S'))
                obj.toDateTimeField = pytz.utc.localize(datetime.strptime(obj.toDate.decode('ascii'), '%Y-%m-%d %H:%M:%S'))
                obj.save()
                print 'Saved Server Record' + str(obj.systemId)
            except Exception, e:
                print obj.systemId
                print str(e)
