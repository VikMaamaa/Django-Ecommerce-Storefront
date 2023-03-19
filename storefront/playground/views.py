from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product, OrderItem
# Create your views here.

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    # order = OrderItem.objects.all()
    # pro = []
    # for a in order:
    #     print(a.product_id)
    #     t = Product.objects.filter(pk=a.product_id).first()
    #     pro.append(t)
    # exists = Product.objects.values('id', 'title', 'collection__title')
    
    exists = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    # print(exists)
    return render(request, 'hello.html', {'name': 'Mosh', 'products':list(exists)})
