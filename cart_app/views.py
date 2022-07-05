import json
from django.http import HttpResponse
from django.shortcuts import redirect, render

from product_app.models import *
from .models import *
from user_app.models import Custom_user
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
# def Add_to_cart(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         if Cart.objects.filter(customer_id=user,product=item):
#             qty=Cart.objects.get(customer_id=user,product=item)
#             qty.qty+=1
#             qty.save()
#         else:
#             add=Cart(customer_id=user,product=item,qty=1)
#             add.save()
#         return redirect(f"/products/{item_id}")
#     else:
#         return redirect("/customer/login")

# def wish_to_cart(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         if Cart.objects.filter(customer_id=user,product=item):
#             qty=Cart.objects.get(customer_id=user,product=item)
#             qty.qty+=1
#             qty.save()
#         else:
#             add=Cart(customer_id=user,product=item,qty=1)
#             add.save()
#         return redirect("/cart/wishlist")
#     else:
#         return redirect("/customer/login")


# def cart_to_wishlist(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         if Wishlist.objects.filter(customer_id=user,product=item):
#             qty=Cart.objects.get(customer_id=user,product=item)
#             qty.delete()
#         else:
#             add=Wishlist(customer_id=user,product=item)
#             add.save()
#             qty=Cart.objects.get(customer_id=user,product=item)
#             qty.delete()
#         return redirect("/cart")
#     else:
#         return redirect("/customer/login")


def cart_to_wishlist(request,item_id):
    item=Product_table.objects.get(id=item_id)
    user=request.session['user']
    cart_item=Cart_table.objects.get(customer_id=user,product=item)
    cart_item.delete()
    request.session['cart_count']=Cart_table.objects.filter(customer_id=user).count()
    if not Wishlist_table.objects.filter(customer_id=user,product=item):
        add=Wishlist_table(customer_id=user,product=item)
        add.save()
        wishlist_count=Wishlist_table.objects.filter(customer_id=user).count()
        request.session['wishlist_count']=wishlist_count
        return JsonResponse({'success':True,'wishlist_count':wishlist_count})
    else:
        return JsonResponse({'success':True})
    


# def delect_from_wishlist(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         item=Wishlist.objects.get(customer_id=user,product=item)
#         item.delete()
#         return redirect("/cart/wishlist")
#     else:
#         return redirect("/customer/login")

def wishlist(request):
    
    return render(request, "wishlist.html")


def add_one_cart(request,item_id):
    if request.method=='GET':
        id=request.session['user']

        if Cart_table.objects.filter(customer_id=id,product_id=item_id):
            old_cart_object=Cart_table.objects.get(customer_id=id,product_id=item_id)
            old_cart_object.qty+=1
            old_cart_object.save()
        else:
            item=Cart_table.objects.create(product_id=item_id, customer_id=id)
            item.save()
        cart_count=Cart_table.objects.filter(customer_id=id).count()
        request.session['cart_count']=cart_count
        return JsonResponse({'success':True,'cart_count':cart_count})
    

# def remove_one_cart(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         if Cart.objects.filter(customer_id=user,product=item)[0].qty==1:
#             qty=Cart.objects.get(customer_id=user,product=item)
#             qty.delete()
#         else:    
#             qty=Cart.objects.get(customer_id=user,product=item)
#             qty.qty-=1
#             qty.save()
#         return redirect('/cart')
#     else:
#         return redirect("/customer/login")

# def delect_from_cart(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         qty=Cart.objects.get(customer_id=user,product=item)
#         qty.delete()    
#         return redirect('/cart')
#     else:
#         return redirect("/customer/login")


def cart(request):
    user=request.session['user']
    items=Cart_table.objects.filter(customer_id=user)
    subtotal=0
    for i in range(len(items)):
        subtotal+=items[i].product.min_price*items[i].qty
    context={
    'cart_items':Cart_table.objects.filter(customer_id=user),
    'subtotal':subtotal,
    }
    return render(request, "cart.html",context)

def wishlist(request):
    context={
    'wishlist_items':Wishlist_table.objects.filter(customer_id=request.session['user'])
    }
    return render(request, "wishlist.html",context)