from django.contrib import admin

# Register your models here.
from case.models import *

# Register your models here.
admin.site.register([Service, Rfo, Onduty, Provider, Customer, Fault, TicketNumber])