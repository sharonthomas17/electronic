from unicodedata import name
from django.shortcuts import render,redirect
from .models import *
from .forms import *

def shop_view(request):
    var=list(Shop.objects.values())
    form=ShopForm()
    d1={'form': form,
        'data': var }
    return render(request,"index.html",d1)

def shop_creat(request):
    form = ShopForm(request.POST)
    if form.is_valid():
        Shop.objects.create(**form.cleaned_data)
        
    return redirect(shop_view)

def shop_delete(request,pk):
    name=Shop.objects.get(id=pk)
    name.delete()
    return redirect(shop_view)



def item_view(request):
    var=list(Elect_shop.objects.values())
    form3=ItemForm()
    d1={'form': form3,
        'data': var }
    return render(request,"disp.html",d1)

def item_creat(request):
    form3 = ItemForm(request.POST)
    if form3.is_valid():
        Elect_shop.objects.create(**form3.cleaned_data)
        
    return redirect(item_view)

def item_delete(request,pk):
    name=list(Elect_shop.objects.get(id=pk))
    name.delete()
    return redirect(item_view)
    
