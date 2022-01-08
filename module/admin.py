from django.contrib import admin

# Register your models here.
from module.models import bill, product

admin.site.register((bill,product))