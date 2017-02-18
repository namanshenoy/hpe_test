# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from dashboard.models import *
import os
import csv
import sys
from datetime import datetime
import pytz


reload(sys)
sys.setdefaultencoding("utf-8")


class Command(BaseCommand):
    def handle(self, *args, **options):
        top = os.getcwd() + '/perform-csv/'
        perform_csv_list = []
        for path, subdirs, files in os.walk(top):
            for filename in files:
                perform_csv_list.append(filename)
        fields_perform_summary = ['serialNumberInserv', 'system_companyName', 'system_model', 'updated',
                                  'system_installDate',
                                  'capacity_total_sizeTiB', 'capacity_total_freePct', 'capacity_byType_fc_sizeTiB',
                                  'capacity_byType_nl_sizeTiB', 'capacity_byType_ssd_sizeTiB',
                                  'capacity_total_dedupeRatio',
                                  'virtualCapacity_byType_tdvv_vvCount', 'virtualCapacity_byType_tdvv_sizeTiB']
        print top
        print perform_csv_list

        for row in csv.reader(open(top + 'perform-summary.csv')):
            print row
            server, found = Server.objects.get_or_create(**dict(zip(fields_perform_summary, row)))
            company_name = row[1]
            company, found = Company.objects.get_or_create(company_name=company_name)
            company.servers.add(server)
            server.save()
            company.save()

        fields_perform_record = ['systemId', 'fromDate', 'toDate', 'tpdKernelPatch', 'tpdKernelPatchPrevious',
                                 'vvCountHistVlun', 'vvCountHistVlunPrevious', 'totalWriteIOsHistVlun',
                                 'totalWriteIOsHistPortTargets', 'delAcks', 'delAcksPct', 'writesGt16s',
                                 'writesGt32msPct', 'writesGt64msPct', 'writesGt128msPct', 'writesGt256msPct',
                                 'writesGt512msPct', 'writesGt1024msPct', 'writesGt2048msPct', 'writesGt4096msPct',
                                 'writes0_062msPct', 'writes0_125msPct', 'writes0_25msPct', 'writes0_5msPct',
                                 'writes1msPct', 'writes2msPct', 'writes4msPct', 'writes8msPct', 'writes16msPct',
                                 'writes32msPct', 'writes64msPct', 'writes128msPct', 'writes256msPct', 'writes512msPct',
                                 'writes1024msPct', 'writes2048msPct', 'writes4096msPct', 'writes8192msPct',
                                 'writes16384msPct', 'writes32768msPct', 'writes65536msPct', 'readsGt32msPct',
                                 'readsGt64msPct', 'readsGt128msPct', 'readsGt256msPct', 'readsGt512msPct',
                                 'readsGt1024msPct', 'readsGt2048msPct', 'readsGt4096msPct', 'reads0_062msPct',
                                 'reads0_125msPct', 'reads0_25msPct', 'reads0_5msPct', 'reads1msPct', 'reads2msPct',
                                 'reads4msPct', 'reads8msPct', 'reads16msPct', 'reads32msPct', 'reads64msPct',
                                 'reads128msPct', 'reads256msPct', 'reads512msPct', 'reads1024msPct', 'reads2048msPct',
                                 'reads4096msPct', 'reads8192msPct', 'reads16384msPct', 'reads32768msPct',
                                 'reads65536msPct', 'totalsGt32msPct', 'totalsGt64msPct', 'totalsGt128msPct',
                                 'totalsGt256msPct', 'totalsGt512msPct', 'totalsGt1024msPct', 'totalsGt2048msPct',
                                 'totalsGt4096msPct', 'totals0_062msPct', 'totals0_125msPct', 'totals0_25msPct',
                                 'totals0_5msPct', 'totals1msPct', 'totals2msPct', 'totals4msPct', 'totals8msPct',
                                 'totals16msPct', 'totals32msPct', 'totals64msPct', 'totals128msPct', 'totals256msPct',
                                 'totals512msPct', 'totals1024msPct', 'totals2048msPct', 'totals4096msPct',
                                 'totals8192msPct', 'totals16384msPct', 'totals32768msPct', 'totals65536msPct',
                                 'portReadBandwidthMBPS', 'portWriteBandwidthMBPS', 'portTotalBandwidthMBPS',
                                 'cpuLatestSysAvgPct', 'cpuLatestUserAvgPct', 'cpuLatestTotalAvgPct',
                                 'cpuLatestSysMaxPct', 'cpuLatestUserMaxPct', 'cpuLatestTotalMaxPct',
                                 'portReadAvgIOSizeKB', 'portWriteAvgIOSizeKB', 'portTotalAvgIOSizeKB',
                                 'ddsSizeUsedTiB', 'nodeUpSinceMostRecent', 'nodeCountOffline', 'nodeCountMissing',
                                 'ddsSizeUsedTiBPrevious']

        for filename in perform_csv_list:
            skip_line1 = False
            print 'Current Server: ' + filename
            if filename != 'perform-summary.csv':
                for row in csv.reader(open(top + filename)):
                    if skip_line1:
                        server_record, found = ServerRecord.objects.get_or_create(**dict(zip(fields_perform_record, row)))
                        system_id = row[0]
                        print row[0]
                        from_date = row[1]
                        to_date = row[2]
                        server_record.toDateTimeField = pytz.utc.localize(
                            datetime.strptime(server_record.toDate.decode('ascii'), '%Y-%m-%d %H:%M:%S'))

                        server_record.fromDateTimeField = pytz.utc.localize(
                            datetime.strptime(server_record.fromDate.decode('ascii'), '%Y-%m-%d %H:%M:%S'))

                        server = Server.objects.get(serialNumberInserv=system_id)
                        server.records.add(server_record)
                        server_record.save()
                        server.save()

                    else:
                        skip_line1 = True
