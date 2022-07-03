from django.http import HttpResponse
from django.shortcuts import redirect, render
from product_app.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt

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


# def add_to_wishlist(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         if Wishlist.objects.filter(customer_id=user,product=item):
#             pass
#         else:
#             add=Wishlist(customer_id=user,product=item)
#             add.save()
#         return redirect(f"/products/{item_id}")
#     else:
#         return redirect("/customer/login")


# def delect_from_wishlist(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         item=Wishlist.objects.get(customer_id=user,product=item)
#         item.delete()
#         return redirect("/cart/wishlist")
#     else:
#         return redirect("/customer/login")

# def wishlist(request):
#     if  request.user.is_authenticated:
#         context={
#         'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id)),
#         'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
#         'wishlist_items':Wishlist.objects.filter(customer_id=request.user.id)
#         }
#         return render(request, "wishlist.html",context)
#     else:
#         return redirect("/customer/login")

# def add_one_cart(request,item_id):
#     if  request.user.is_authenticated:
#         item=Product.objects.get(id=item_id)
#         user=request.user.id
#         qty=Cart.objects.get(customer_id=user,product=item)
#         qty.qty+=1
#         qty.save()
#         return redirect("/cart")
#     else:
#         return redirect("/customer/login")


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


# def cart(request):
#     if  request.user.is_authenticated:
#         user=request.user.id
#         items=Cart.objects.filter(customer_id=user)
#         subtotal=float()
#         for i in range(len(items)):
#             subtotal+=items[i].product.price*items[i].qty
#         context={
#         'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
#         'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id)),
#         'cart_items':Cart.objects.filter(customer_id=request.user.id),
#         'subtotal':subtotal,
#         'total':subtotal+100
#         }
#         return render(request, "cart.html",context)
#     else:
#         return redirect("/customer/login")