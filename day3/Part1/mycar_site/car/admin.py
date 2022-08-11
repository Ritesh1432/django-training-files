from django.contrib import admin
from car.models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TIME INFORMATION',{'fields':['year']}),
        ('CAR INFORMATION',{'fields':['brand']}),


    ]

admin.site.register(Car,CarAdmin)