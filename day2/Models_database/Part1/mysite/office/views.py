from django.shortcuts import render
from office.models import Patient

# Create your views here.
def office_view(request):
    office = Patient.objects.all()
    context = {'office':office}
    return render(request,'office.html',context=context)