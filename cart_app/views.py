from django.shortcuts import render,redirect
from product_app.models import *
from user_app.dec import *
from wishlist_app.models import *
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse

@login_is_required
def cart_to_wishlist(request,item_id):
    item=Product_table.objects.filter(id=item_id)
    user=request.session['user']

    if not Wishlist_table.objects.filter(customer_id=user,product_id=item[0].id):
        add=Wishlist_table(customer_id=user,product_id=item[0].id)
        add.save()
        wishlist_count=Wishlist_table.objects.filter(customer_id=user).count()
        request.session['wishlist_count']=wishlist_count
        cart_item=Cart_table.objects.filter(customer_id=user,product_id=item[0].id)
        cart_item[0].delete()
        request.session['cart_count']=Cart_table.objects.filter(customer_id=user).count()

        return JsonResponse({'success':True,'wishlist_count':wishlist_count, 'cart_count':request.session['cart_count']})
    else:
        return JsonResponse({'success':True,'cart_count':request.session['cart_count']})
    
@login_is_required
def add_new_cart(request,item_id):
    if request.method=='GET':
        id=request.session['user']
        if Cart_table.objects.filter(customer_id=id,product_id=item_id):
            old_cart_object=Cart_table.objects.get(customer_id=id,product_id=item_id)
            old_cart_object.qty+=1
            old_cart_object.save()
        else:
            item=Cart_table.objects.create(product_id=item_id, qty=1, customer_id=id)
            item.save()
        cart_count=Cart_table.objects.filter(customer_id=id).count()
        request.session['cart_count']=cart_count
        return JsonResponse({'success':True,'cart_count':cart_count})
    
@login_is_required
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

@login_is_required
def delect_from_cart(request,item_id):
    user=request.session['user']
    if Cart_table.objects.filter(id=item_id):
        item=Cart_table.objects.get(id=item_id)
        item.delete()

        cart_count=Cart_table.objects.filter(customer_id=user).count()
        request.session['cart_count']=cart_count
        return JsonResponse({'success':True,'count':True,'cart_count':cart_count})
    else:
        return HttpResponse('<h1>server error</h1>')
    
@login_is_required
def add_one_cart(request,item_id):
    item=Product_table.objects.get(id=item_id)
    user=request.session['user']
    cart_item=Cart_table.objects.get(customer_id=user,product=item)
    cart_item.qty=cart_item.qty+1
    count=cart_item.qty
    cart_item.save()
    return JsonResponse({'success':True,'count':count})

@login_is_required
def remove_one_cart(request,item_id):
    item=Product_table.objects.get(id=item_id)
    user=request.session['user']
    cart_item=Cart_table.objects.get(customer_id=user,product=item)
    cart_item.qty=cart_item.qty-1
    count=cart_item.qty
    if count==0:
        cart_item.delete()
        return JsonResponse({'success':True,'count_zero':True})
    else:
        cart_item.save()
        return JsonResponse({'success':True,'count':count})