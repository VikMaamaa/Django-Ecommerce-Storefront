from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.db.models import Value
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg,  Sum

from store.models import Product, OrderItem, Order, Customer
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
    
    # exists = Product.objects.prefetch_related('promotions').select_related('collection').all()
    
    
    
    # print(exists)
    # exists = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # exists = Product.objects.filter(collection__id=1).aggregate(Count('id'), min_price=Min('unit_price'))
    
    
    exists = Customer.objects.annotate(new_id=F('id') +1)
    return render(request, 'hello.html', {'name': 'Mosh', 'results': exists})
