from django.contrib import admin
# from .models import Banner,ServiceCategory, Service
from .models import *
# Register your models here.

table = [Banner,ServiceCategory,Service,ContactUs]
admin.site.register(table)