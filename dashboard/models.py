from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class ServerRecord(models.Model):
    systemId = models.CharField(db_index=True, max_length=128, blank=False, null=False, default="0")

    #fromDate = models.CharField(max_length=128, blank=True, null=True)
    fromDate = models.DateField(blank=True, null=True)

    #toDate = models.CharField(max_length=128, blank=True, null=True)
    toDate = models.DateTimeField(blank=True, null=True)

    tpdKernelPatch = models.CharField(max_length=128, blank=True, null=True)
    tpdKernelPatchPrevious = models.CharField(max_length=128, blank=True, null=True)
    vvCountHistVlun = models.CharField(max_length=128, blank=True, null=True)
    vvCountHistVlunPrevious = models.CharField(max_length=128, blank=True, null=True)
    totalWriteIOsHistVlun = models.CharField(max_length=128, blank=True, null=True)
    totalWriteIOsHistPortTargets = models.CharField(max_length=128, blank=True, null=True)
    delAcks = models.CharField(max_length=128, blank=True, null=True)
    delAcksPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt16s = models.CharField(max_length=128, blank=True, null=True)
    writesGt32msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt64msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt128msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt256msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt512msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt1024msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt2048msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt4096msPct = models.CharField(max_length=128, blank=True, null=True)
    writes0_062msPct = models.CharField(max_length=128, blank=True, null=True)
    writes0_125msPct = models.CharField(max_length=128, blank=True, null=True)
    writes0_25msPct = models.CharField(max_length=128, blank=True, null=True)
    writes0_5msPct = models.CharField(max_length=128, blank=True, null=True)
    writes1msPct = models.CharField(max_length=128, blank=True, null=True)
    writes2msPct = models.CharField(max_length=128, blank=True, null=True)
    writes4msPct = models.CharField(max_length=128, blank=True, null=True)
    writes8msPct = models.CharField(max_length=128, blank=True, null=True)
    writes16msPct = models.CharField(max_length=128, blank=True, null=True)
    writes32msPct = models.CharField(max_length=128, blank=True, null=True)
    writes64msPct = models.CharField(max_length=128, blank=True, null=True)
    writes128msPct = models.CharField(max_length=128, blank=True, null=True)
    writes256msPct = models.CharField(max_length=128, blank=True, null=True)
    writes512msPct = models.CharField(max_length=128, blank=True, null=True)
    writes1024msPct = models.CharField(max_length=128, blank=True, null=True)
    writes2048msPct = models.CharField(max_length=128, blank=True, null=True)
    writes4096msPct = models.CharField(max_length=128, blank=True, null=True)
    writes8192msPct = models.CharField(max_length=128, blank=True, null=True)
    writes16384msPct = models.CharField(max_length=128, blank=True, null=True)
    writes32768msPct = models.CharField(max_length=128, blank=True, null=True)
    writes65536msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt32msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt64msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt128msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt256msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt512msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt1024msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt2048msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt4096msPct = models.CharField(max_length=128, blank=True, null=True)
    reads0_062msPct = models.CharField(max_length=128, blank=True, null=True)
    reads0_125msPct = models.CharField(max_length=128, blank=True, null=True)
    reads0_25msPct = models.CharField(max_length=128, blank=True, null=True)
    reads0_5msPct = models.CharField(max_length=128, blank=True, null=True)
    reads1msPct = models.CharField(max_length=128, blank=True, null=True)
    reads2msPct = models.CharField(max_length=128, blank=True, null=True)
    reads4msPct = models.CharField(max_length=128, blank=True, null=True)
    reads8msPct = models.CharField(max_length=128, blank=True, null=True)
    reads16msPct = models.CharField(max_length=128, blank=True, null=True)
    reads32msPct = models.CharField(max_length=128, blank=True, null=True)
    reads64msPct = models.CharField(max_length=128, blank=True, null=True)
    reads128msPct = models.CharField(max_length=128, blank=True, null=True)
    reads256msPct = models.CharField(max_length=128, blank=True, null=True)
    reads512msPct = models.CharField(max_length=128, blank=True, null=True)
    reads1024msPct = models.CharField(max_length=128, blank=True, null=True)
    reads2048msPct = models.CharField(max_length=128, blank=True, null=True)
    reads4096msPct = models.CharField(max_length=128, blank=True, null=True)
    reads8192msPct = models.CharField(max_length=128, blank=True, null=True)
    reads16384msPct = models.CharField(max_length=128, blank=True, null=True)
    reads32768msPct = models.CharField(max_length=128, blank=True, null=True)
    reads65536msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt32msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt64msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt128msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt256msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt512msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt1024msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt2048msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt4096msPct = models.CharField(max_length=128, blank=True, null=True)
    totals0_062msPct = models.CharField(max_length=128, blank=True, null=True)
    totals0_125msPct = models.CharField(max_length=128, blank=True, null=True)
    totals0_25msPct = models.CharField(max_length=128, blank=True, null=True)
    totals0_5msPct = models.CharField(max_length=128, blank=True, null=True)
    totals1msPct = models.CharField(max_length=128, blank=True, null=True)
    totals2msPct = models.CharField(max_length=128, blank=True, null=True)
    totals4msPct = models.CharField(max_length=128, blank=True, null=True)
    totals8msPct = models.CharField(max_length=128, blank=True, null=True)
    totals16msPct = models.CharField(max_length=128, blank=True, null=True)
    totals32msPct = models.CharField(max_length=128, blank=True, null=True)
    totals64msPct = models.CharField(max_length=128, blank=True, null=True)
    totals128msPct = models.CharField(max_length=128, blank=True, null=True)
    totals256msPct = models.CharField(max_length=128, blank=True, null=True)
    totals512msPct = models.CharField(max_length=128, blank=True, null=True)
    totals1024msPct = models.CharField(max_length=128, blank=True, null=True)
    totals2048msPct = models.CharField(max_length=128, blank=True, null=True)
    totals4096msPct = models.CharField(max_length=128, blank=True, null=True)
    totals8192msPct = models.CharField(max_length=128, blank=True, null=True)
    totals16384msPct = models.CharField(max_length=128, blank=True, null=True)
    totals32768msPct = models.CharField(max_length=128, blank=True, null=True)
    totals65536msPct = models.CharField(max_length=128, blank=True, null=True)
    portReadBandwidthMBPS = models.CharField(max_length=128, blank=True, null=True)
    portWriteBandwidthMBPS = models.CharField(max_length=128, blank=True, null=True)
    portTotalBandwidthMBPS = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestSysAvgPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestUserAvgPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestTotalAvgPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestSysMaxPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestUserMaxPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestTotalMaxPct = models.CharField(max_length=128, blank=True, null=True)
    portReadAvgIOSizeKB = models.CharField(max_length=128, blank=True, null=True)
    portWriteAvgIOSizeKB = models.CharField(max_length=128, blank=True, null=True)
    portTotalAvgIOSizeKB = models.CharField(max_length=128, blank=True, null=True)
    ddsSizeUsedTiB = models.CharField(max_length=128, blank=True, null=True)
    nodeUpSinceMostRecent = models.CharField(max_length=128, blank=True, null=True)
    nodeCountOffline = models.CharField(max_length=128, blank=True, null=True)
    nodeCountMissing = models.CharField(max_length=128, blank=True, null=True)
    ddsSizeUsedTiBPrevious = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = ['toDate']

    def __str__(self):
        return self.systemId + ' ' + str(self.fromDate)

    def __unicode__(self):
        return self.systemId + ' ' + str(self.fromDate)

class HealthscoreFactors(models.Model):
    systemId = models.CharField(db_index=True, max_length=128, blank=False, null=False, default="0")
    healthscore = models.IntegerField(default=100)
    capacity_total_freePct = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    delAcksPct = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    portReadBandwidthMBPS = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    portWriteBandwidthMBPS = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    cpuLatestTotalAvgPct = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    cpuLatestTotalMaxPct = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    nodeCountOffline = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    nodeCountMissing = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)
    ddsSizeUsedTiB = models.DecimalField(default=0.0, max_digits=10, decimal_places=3)

    class Meta:
        ordering = ['systemId']

    def __str__(self):
        return self.systemId + ' ' + str(self.healthscore)

    def __unicode__(self):
        return self.systemId + ' ' + str(self.healthScore)

class Server(models.Model):
    serialNumberInserv = models.IntegerField(default=0, primary_key=True)
    system_companyName = models.CharField(db_index=True, max_length=128, blank=True, null=True)
    system_model = models.CharField(max_length=128, blank=True, null=True)
    updated = models.DateField(max_length=128, blank=True, null=True)
    system_installDate = models.CharField(max_length=128, blank=True, null=True)
    capacity_total_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    capacity_total_freePct = models.CharField(max_length=128, blank=True, null=True)
    capacity_byType_fc_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    capacity_byType_nl_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    capacity_byType_ssd_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    capacity_total_dedupeRatio = models.CharField(max_length=128, blank=True, null=True)
    virtualCapacity_byType_tdvv_vvCount = models.CharField(max_length=128, blank=True, null=True)
    virtualCapacity_byType_tdvv_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    healthscore = models.ForeignKey(HealthscoreFactors, null=True, blank=True)

    class Meta:
        ordering = ['serialNumberInserv']

    def __str__(self):
        return self.system_companyName + ' ' + str(self.serialNumberInserv)

    def __unicode__(self):
        return self.system_companyName + ' ' + str(self.serialNumberInserv)


class Company(models.Model):
    user = models.ManyToManyField(User, blank=True)
    company_name = models.CharField(max_length=128, blank=True, null=True)
    servers = models.ManyToManyField(Server)

    def __str__(self):
        return self.company_name

    def __unicode__(self):
        return self.company_name


class Averages(models.Model):
    system_model = models.CharField(max_length=128, blank=True, null=True)

    # process-summary
    capacity_total_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    capacity_total_freePct = models.CharField(max_length=128, blank=True, null=True)
    capacity_byType_fc_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    capacity_byType_nl_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    capacity_byType_ssd_sizeTiB = models.CharField(max_length=128, blank=True, null=True)
    capacity_total_dedupeRatio = models.CharField(max_length=128, blank=True, null=True)
    virtualCapacity_byType_tdvv_vvCount = models.CharField(max_length=128, blank=True, null=True)
    virtualCapacity_byType_tdvv_sizeTiB = models.CharField(max_length=128, blank=True, null=True)

    # server-summary
    tpdKernelPatch = models.CharField(max_length=128, blank=True, null=True)
    tpdKernelPatchPrevious = models.CharField(max_length=128, blank=True, null=True)
    vvCountHistVlun = models.CharField(max_length=128, blank=True, null=True)
    vvCountHistVlunPrevious = models.CharField(max_length=128, blank=True, null=True)
    totalWriteIOsHistVlun = models.CharField(max_length=128, blank=True, null=True)
    totalWriteIOsHistPortTargets = models.CharField(max_length=128, blank=True, null=True)
    delAcks = models.CharField(max_length=128, blank=True, null=True)
    delAcksPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt16s = models.CharField(max_length=128, blank=True, null=True)
    writesGt32msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt64msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt128msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt256msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt512msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt1024msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt2048msPct = models.CharField(max_length=128, blank=True, null=True)
    writesGt4096msPct = models.CharField(max_length=128, blank=True, null=True)
    writes0_062msPct = models.CharField(max_length=128, blank=True, null=True)
    writes0_125msPct = models.CharField(max_length=128, blank=True, null=True)
    writes0_25msPct = models.CharField(max_length=128, blank=True, null=True)
    writes0_5msPct = models.CharField(max_length=128, blank=True, null=True)
    writes1msPct = models.CharField(max_length=128, blank=True, null=True)
    writes2msPct = models.CharField(max_length=128, blank=True, null=True)
    writes4msPct = models.CharField(max_length=128, blank=True, null=True)
    writes8msPct = models.CharField(max_length=128, blank=True, null=True)
    writes16msPct = models.CharField(max_length=128, blank=True, null=True)
    writes32msPct = models.CharField(max_length=128, blank=True, null=True)
    writes64msPct = models.CharField(max_length=128, blank=True, null=True)
    writes128msPct = models.CharField(max_length=128, blank=True, null=True)
    writes256msPct = models.CharField(max_length=128, blank=True, null=True)
    writes512msPct = models.CharField(max_length=128, blank=True, null=True)
    writes1024msPct = models.CharField(max_length=128, blank=True, null=True)
    writes2048msPct = models.CharField(max_length=128, blank=True, null=True)
    writes4096msPct = models.CharField(max_length=128, blank=True, null=True)
    writes8192msPct = models.CharField(max_length=128, blank=True, null=True)
    writes16384msPct = models.CharField(max_length=128, blank=True, null=True)
    writes32768msPct = models.CharField(max_length=128, blank=True, null=True)
    writes65536msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt32msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt64msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt128msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt256msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt512msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt1024msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt2048msPct = models.CharField(max_length=128, blank=True, null=True)
    readsGt4096msPct = models.CharField(max_length=128, blank=True, null=True)
    reads0_062msPct = models.CharField(max_length=128, blank=True, null=True)
    reads0_125msPct = models.CharField(max_length=128, blank=True, null=True)
    reads0_25msPct = models.CharField(max_length=128, blank=True, null=True)
    reads0_5msPct = models.CharField(max_length=128, blank=True, null=True)
    reads1msPct = models.CharField(max_length=128, blank=True, null=True)
    reads2msPct = models.CharField(max_length=128, blank=True, null=True)
    reads4msPct = models.CharField(max_length=128, blank=True, null=True)
    reads8msPct = models.CharField(max_length=128, blank=True, null=True)
    reads16msPct = models.CharField(max_length=128, blank=True, null=True)
    reads32msPct = models.CharField(max_length=128, blank=True, null=True)
    reads64msPct = models.CharField(max_length=128, blank=True, null=True)
    reads128msPct = models.CharField(max_length=128, blank=True, null=True)
    reads256msPct = models.CharField(max_length=128, blank=True, null=True)
    reads512msPct = models.CharField(max_length=128, blank=True, null=True)
    reads1024msPct = models.CharField(max_length=128, blank=True, null=True)
    reads2048msPct = models.CharField(max_length=128, blank=True, null=True)
    reads4096msPct = models.CharField(max_length=128, blank=True, null=True)
    reads8192msPct = models.CharField(max_length=128, blank=True, null=True)
    reads16384msPct = models.CharField(max_length=128, blank=True, null=True)
    reads32768msPct = models.CharField(max_length=128, blank=True, null=True)
    reads65536msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt32msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt64msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt128msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt256msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt512msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt1024msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt2048msPct = models.CharField(max_length=128, blank=True, null=True)
    totalsGt4096msPct = models.CharField(max_length=128, blank=True, null=True)
    totals0_062msPct = models.CharField(max_length=128, blank=True, null=True)
    totals0_125msPct = models.CharField(max_length=128, blank=True, null=True)
    totals0_25msPct = models.CharField(max_length=128, blank=True, null=True)
    totals0_5msPct = models.CharField(max_length=128, blank=True, null=True)
    totals1msPct = models.CharField(max_length=128, blank=True, null=True)
    totals2msPct = models.CharField(max_length=128, blank=True, null=True)
    totals4msPct = models.CharField(max_length=128, blank=True, null=True)
    totals8msPct = models.CharField(max_length=128, blank=True, null=True)
    totals16msPct = models.CharField(max_length=128, blank=True, null=True)
    totals32msPct = models.CharField(max_length=128, blank=True, null=True)
    totals64msPct = models.CharField(max_length=128, blank=True, null=True)
    totals128msPct = models.CharField(max_length=128, blank=True, null=True)
    totals256msPct = models.CharField(max_length=128, blank=True, null=True)
    totals512msPct = models.CharField(max_length=128, blank=True, null=True)
    totals1024msPct = models.CharField(max_length=128, blank=True, null=True)
    totals2048msPct = models.CharField(max_length=128, blank=True, null=True)
    totals4096msPct = models.CharField(max_length=128, blank=True, null=True)
    totals8192msPct = models.CharField(max_length=128, blank=True, null=True)
    totals16384msPct = models.CharField(max_length=128, blank=True, null=True)
    totals32768msPct = models.CharField(max_length=128, blank=True, null=True)
    totals65536msPct = models.CharField(max_length=128, blank=True, null=True)
    portReadBandwidthMBPS = models.CharField(max_length=128, blank=True, null=True)
    portWriteBandwidthMBPS = models.CharField(max_length=128, blank=True, null=True)
    portTotalBandwidthMBPS = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestSysAvgPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestUserAvgPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestTotalAvgPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestSysMaxPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestUserMaxPct = models.CharField(max_length=128, blank=True, null=True)
    cpuLatestTotalMaxPct = models.CharField(max_length=128, blank=True, null=True)
    portReadAvgIOSizeKB = models.CharField(max_length=128, blank=True, null=True)
    portWriteAvgIOSizeKB = models.CharField(max_length=128, blank=True, null=True)
    portTotalAvgIOSizeKB = models.CharField(max_length=128, blank=True, null=True)
    ddsSizeUsedTiB = models.CharField(max_length=128, blank=True, null=True)
    nodeUpSinceMostRecent = models.CharField(max_length=128, blank=True, null=True)
    nodeCountOffline = models.CharField(max_length=128, blank=True, null=True)
    nodeCountMissing = models.CharField(max_length=128, blank=True, null=True)
    ddsSizeUsedTiBPrevious = models.CharField(max_length=128, blank=True, null=True)
