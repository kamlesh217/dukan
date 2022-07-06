from django.shortcuts import render,redirect
from cart_app.models import *
from product_app.models import *
from django.http import JsonResponse
from wishlist_app.models import *
from django.http import HttpResponse

# Create your views here.

def wishlist(request):
    context={
    'wishlist_items':Wishlist_table.objects.filter(customer_id=request.session['user'])
    }
    return render(request, "wishlist.html",context)

def wish_to_cart(request,item_id):

    item=Product_table.objects.get(id=item_id)
    user=request.session['user']

    if not  Cart_table.objects.filter(customer_id=user,product=item):
        add=Cart_table(customer_id=user,product=item,qty=1)
        add.save()
        cart_count=Cart_table.objects.filter(customer_id=user).count()
        request.session['cart_count']=cart_count
        return JsonResponse({'success':True,'cart_count':cart_count})
    else:
        return JsonResponse({'success':True})

def delect_from_wishlist(request,item_id):
    user=request.session['user']
    if Wishlist_table.objects.filter(id=item_id):
        item=Wishlist_table.objects.get(id=item_id)
        item.delete()

        wishlist_count=Wishlist_table.objects.filter(customer_id=user).count()
        request.session['wishlist_count']=wishlist_count
        return JsonResponse({'success':True,'count':True,'wishlist_count':wishlist_count})
    else:
        return HttpResponse('<h1>server error</h1>')
