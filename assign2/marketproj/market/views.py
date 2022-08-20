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
        desc = request.POST['desc']
        #print(itemname,barcode,price)
        for i in models.User.objects.all():
            if i.username == request.POST.get('owner'):
                owner = i
        models.Item.objects.create(itemname=itemname,barcode=barcode,price=price,desc = desc,owner = owner)
        return redirect(reverse('market:market'))
    else:
        context = {'users':models.User.objects.all()}
        return render(request,'market/add.html',context=context)

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
    own_items = []
    all_items = []
    fetched_items = list(models.Item.objects.all())
    for itm in fetched_items:
        if request.session.get('username') == str(itm.owner):
            own_items.append(itm)
    for i in fetched_items:
        if request.session.get('username') != str(i.owner):
            all_items.append(i)    
    context = {'all_items':all_items,'owner_items':own_items}
    return render(request,'market/market.html',context=context)

def sell_view(request,item_id):
    rec = models.Item.objects.get(id = item_id)
    userrec = models.User.objects.get(username = request.session.get('username'))
    userrec.budget += rec.price
    request.session['budget'] = userrec.budget
    rec.owner = None
    rec.save()
    userrec.save()
    return redirect(reverse('market:market'))

def purchase_view(request,item_id):
    rec = models.Item.objects.get(id=item_id)
    userrec = models.User.objects.get(username = request.session.get('username'))
    userrec.budget -= rec.price
    request.session['budget'] = userrec.budget
    rec.owner = models.User.objects.get(username = request.session.get('username'))
    rec.save()
    userrec.save()
    return redirect(reverse('market:market'))
