from django.shortcuts import render
from django.db.models import Q, F, Func, DecimalField
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.db import transaction
from django.db.models import Value, ExpressionWrapper
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg,  Sum

from store.models import Product, OrderItem, Order, Customer, Collection
# Create your views here.

def calculate():
    x = 1
    y = 2
    return x

@transaction.atomic
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
    
    
    # exists = Customer.objects.annotate(
    #     full_name = Func(F('first_name'),Value(' ') ,F('last_name'), function='CONCAT')
    # )
    
    # exists = Customer.objects.annotate(
    #     full_name = Concat('first_name',Value(' ') ,'last_name')
    # )
    
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # exists = Product.objects.annotate(
        
    #     discounted_price = discounted_price
    # )
    # print(exists)
    
    # collection = Collection.objects.get(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()
    # collection.id
    
    # collection = Collection.objects.filter(pk=11).update(featured_product=None)
    
    
    # collection = Collection(pk=11)
    # collection.delete()
    
    # Collection.objects.filter(id__gt=5).delete()
   
    # print(collection)
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()
        
        
        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()
    # return render(request, 'hello.html', {'name': 'Mosh', 'results': exists})
