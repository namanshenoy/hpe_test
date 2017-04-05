from django.contrib import admin

# Register your models here.
from dashboard.models import *


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('company_name',)

admin.site.register(Server)
admin.site.register(Company, CompanyAdmin)
admin.site.register(ServerRecord)
