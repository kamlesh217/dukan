from django.shortcuts import render
from cart_app.models import Cart_table
from product_app.models import Product_table

from seller_app.dec import *
from user_app.models import Custom_user
from wishlist_app.models import Wishlist_table

# Create your views here.
@seller_login_is_required
def Seller_dashboard(request):
    product_list=Product_table.objects.filter(supplier_id=request.session['seller'])
    print(product_list)
    return render(request, 'seller/dashboard.html',{"products":product_list})

@seller_logout_is_required
def Sign_up_seller(request):
    try:
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST["email"]
            password=request.POST["password"]
            if Custom_user.objects.filter(email=email,is_seller=True,id_deleted=False):
                messages.success(request, 'Email already Exists')
                return redirect('/seller/sign_up_user')
            else:
                user=Custom_user.objects.create(is_seller=True,id_deleted=False,email=email, first_name=fname, last_name=lname, password=password)
                user.save()
                request.session['first_name']=fname
                request.session['seller_is_active']=True
                request.session['seller']=user[0].id
                # request.session['placed_count']
                
                
                return redirect('/seller')
        return render(request, "seller/sign_up.html")   

    except:
        return HttpResponse('<h1> server error</h1>')

@seller_logout_is_required
def Sign_in_seller(request):
    try:

        if request.method=="POST":
            email=request.POST["email"]
            password=request.POST["password"]
            
            user=Custom_user.objects.filter(is_seller=True,email=email)
            if not user:
                messages.success(request, 'Email not registred')
                return redirect('/seller/sign_in_user')
            else:
                if user[0].password==password:
                    request.session['first_name']=user[0].first_name
                    request.session['seller_is_active']=True
                    request.session['seller']=user[0].id
                    # request.session['placed_count']=Cart_table.objects.filter(customer_id=user[0].id).count()
                    
                    return redirect('/seller')
                else:
                    messages.success(request, 'incorrect password')
                    return redirect('/seller/sign_in_user')

        return render(request, "seller/sign_in.html")
    except:
        return HttpResponse('<h1> server error</h1>')


@seller_login_is_required
def Sign_out_seller(request):
    try:
        request.session.clear()
        return  redirect('/seller')
    except:
        return HttpResponse('<h1> server error</h1>')

@seller_login_is_required
def Order_list(request):
    order_list=8
    return render(request, "seller/order_list.html")

@seller_login_is_required
def Add_new_product(request):
    return render(request, 'seller/add_new.html')