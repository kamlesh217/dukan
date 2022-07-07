from django.shortcuts import render,redirect

from cart_app.models import *
from user_app.dec import *
from .models import *

# Create your views here.

@login_is_required
def checkout(request):
    user=request.session['user']
    item_list=Cart_table.objects.filter(customer_id=user)
    subtotal=0
    for i in range(len(item_list)):
        subtotal+=item_list[i].product.min_price*item_list[i].qty

    context={'item':item_list,
    'subtotal':subtotal,
    'total':subtotal+100,
    }

    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        city=request.POST["city"]
        zip=request.POST["pincode"]
        state=request.POST["state"]
        email=request.POST["email"]

        if OrderDetails.objects.all():
            orderNo=OrderDetails.objects.all().reverse()[0].orderNo+1
        else:
            orderNo=1
        a=orderNo

        order_details=OrderDetails(name=name,customer=user,phone=phone,
        address=address,city=city,zipcode=zip,state=state,email=email,
        orderNo=a,total=subtotal+100)
        order_details.save()

        for item in range(len(item_list)):
            items=OrderItems(qty=item_list[i].qty, totalPrice=item_list[i].product.min_price*item_list[i].qty,
            productID=item_list[0].product,order= order_details)
            items.save()
        
        item_list.delete()
        return redirect("/order")        
    return render(request, "checkout.html", context)

@login_is_required
def orders(request):
    context=[]
    order_list=OrderItems.objects.filter(order__customer=request.session['user'])
    context={
        "order_list":order_list,
        }
    return render(request, "orders.html",context)
