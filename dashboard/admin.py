from django.contrib import admin

# Register your models here.
from dashboard.models import *

admin.site.register(Server)
admin.site.register(Company)
admin.site.register(ServerRecord)