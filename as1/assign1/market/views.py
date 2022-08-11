from multiprocessing import context
from django.shortcuts import render,redirect
from django.urls import reverse
from . import models

# Create your views here.
def add_view(request):
    if request.POST:
        itemname = request.POST['itemname']
        barcode = int(request.POST['barcode'])
        price = int(request.POST['price'])
        #print(itemname,barcode,price)
        models.Item.objects.create(itemname=itemname,barcode=barcode,price=price)
        return redirect(reverse('market:market'))
    else:
        return render(request,'market/add.html')

def delete_view(request):
    if request.POST:
        itemname = request.POST['itemname']
        try:
            del_items = models.Item.objects.filter(itemname = itemname)
            del_items.delete()
            return redirect(reverse('market:market'))
        except:
            print('PK does not exist')
            return redirect(reverse('market:market'))

    return render(request,'market/delete.html')

def market_view(request):
    all_items = models.Item.objects.all()
    context = {'all_items':all_items}
    return render(request,'market/market.html',context=context)