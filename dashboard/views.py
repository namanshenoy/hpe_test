from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from models import *


@login_required()
def index(request):
    context = {}
    current_user = request.user

    try:
        user_company = Company.objects.get(user=request.user)
        context['company_name'] = str(user_company)

    except ObjectDoesNotExist:
        return render(request, 'index.html', context)
    computers = Server.objects.filter(company=user_company)
    context['computers'] = computers

    return render(request, 'index.html', context)

@csrf_exempt
def api(request):
    if request.POST:
        print request.POST
    return render(request, 'index.html', {})

@login_required()
def detail(request, server_serial):
    context = {}
    current_user = request.user
    try:
        current_company = Company.objects.filter(user=current_user).last()
        company_servers = current_company.servers
        context['company_name'] = str(current_company)
        current_server = current_company.servers.filter(serialNumberInserv=server_serial).first()

        context['current_server'] = current_server
        server_records = ServerRecord.objects.filter(systemId=server_serial)
        latest_server_record = server_records.last()

        context['all_server_records'] = server_records
        dedupe_size_list = []
        record_date_list = []
        for record in server_records:
            print record
            try:
                dds_size = 0.0
                print 'ddsSizeUsed ' + str(record.ddsSizeUsedTiB)
                if record.ddsSizeUsedTiB:
                     dds_size = float(record.ddsSizeUsedTiB)
                record_date_list.append(record.toDate)
                dedupe_size_list.append(dds_size)
            except ValueError:
                print record.ddSizeUsedTiB
                pass

        context['all_server_records_dedupe_size'] = dedupe_size_list
        context['all_server_records_date'] = record_date_list

        context['latest_server_record'] = latest_server_record
        print latest_server_record

    except Exception, e:
        print str(e)
        current_company = None
        current_server = None
        return render(request, 'detail.html', context)

    return render(request, 'detail.html', context)
