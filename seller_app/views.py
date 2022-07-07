from django.shortcuts import render
from cart_app.models import Cart_table

from seller_app.dec import *
from user_app.models import Custom_user
from wishlist_app.models import Wishlist_table

# Create your views here.
@seller_login_is_required
def Seller_dashboard(request):
    return render(request, 'seller/dashboard.html')

@seller_logout_is_required
def Sign_up(request):
    try:
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST["email"]
            password=request.POST["password"]
            if Custom_user.objects.filter(email=email,is_seller=True,id_deleted=False):
                messages.success(request, 'Email already Exists')
                return redirect('/user/sign_up_user')
            else:
                user=Custom_user.objects.create(id_deleted=False,email=email, first_name=fname, last_name=lname, password=password)
                user.save()
                request.session['is_active']=True
                request.session['first_name']=fname
                request.session['seller_is_active']=True
                request.session['user']=user[0].id
                request.session['cart_count']=Cart_table.objects.filter(customer_id=id).count()
                request.session['wishlist_count']=Wishlist_table.objects.filter(customer_id=id).count()
                
                return redirect('/seller')
        return render(request, "seller/sign_up.html")   

    except:
        return HttpResponse('<h1> server error</h1>')

@seller_logout_is_required
def Sign_in(request):
    try:

        if request.method=="POST":
            email=request.POST["email"]
            password=request.POST["password"]
            
            user=Custom_user.objects.filter(email=email)
            if not user:
                messages.success(request, 'Email not registred')
                return redirect('/user/sign_in_user')
            else:
                if user[0].password==password:
                    request.session['is_active']=True
                    request.session['first_name']=user[0].first_name
                    request.session['is_admin']=user[0].is_admin
                    request.session['is_seller']=user[0].is_seller
                    request.session['user']=user[0].id
                    request.session['cart_count']=Cart_table.objects.filter(customer_id=user[0].id).count()
                    request.session['wishlist_count']=Wishlist_table.objects.filter(customer_id=user[0].id).count()
                    return redirect('/')
                else:
                    messages.success(request, 'incorrect password')
                    return redirect('/user/sign_in_user')

        return render(request, "seller/sign_in.html")
    except:
        return HttpResponse('<h1> server error</h1>')


@seller_login_is_required
def Sign_out(request):
    try:
        request.session.clear()
        return  redirect('/')
    except:
        return HttpResponse('<h1> server error</h1>')