from django.contrib import admin
from . models import Review
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
    ('First Name Information',{'fields':['first_name' ,'last_name']}),
    # ('Last Name Information',{'fields':['last_name']}),
    ('Review Information',{'fields':['stars']})
    ]
admin.site.register(Review, ReviewAdmin)
