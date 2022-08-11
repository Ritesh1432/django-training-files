from django.shortcuts import render,redirect
from django.urls import reverse
from . import models

# Create your views here.
def home_view(request):
    return render(request,'car/home.html')

def list_view(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}
    return render(request,'car/list.html',context=context)

def add_view(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        print(brand,year)
        models.Car.objects.create(brand=brand,year = year)
        return redirect(reverse('car:list'))
    else:
        return render(request,'car/add.html')

def delete_view(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk = pk).delete()
            return redirect(reverse('car:list'))
        except:
            print('PK not found')
            return redirect(reverse('car:list'))

    return render(request,'car/delete.html')