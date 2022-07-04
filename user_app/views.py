from django.http.response import HttpResponse
from django.contrib import messages
from .dec import login_is_required, logout_is_required
from user_app.models import Custom_user
from django.shortcuts import redirect,render

@logout_is_required
def Sign_up(request):
    try:
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST["email"]
            password=request.POST["password"]
            if Custom_user.objects.filter(email=email,id_deleted=False):
                messages.success(request, 'Email already Exists')
                return redirect('/user/sign_up_user')
            else:
                user=Custom_user.objects.create(id_deleted=False,email=email, first_name=fname, last_name=lname, password=password)
                user.save()
                request.session['is_active']=True
                request.session['first_name']=fname
                request.session['is_admin']=user.is_admin
                request.session['is_seller']=user.is_seller
                request.session['user']=user[0].id

                return redirect('/')
        return render(request, "register.html")   

    except:
        return HttpResponse('<h1> server error</h1>')

@logout_is_required
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
                    return redirect('/')
                else:
                    messages.success(request, 'incorrect password')
                    return redirect('/user/sign_in_user')

        return render(request, "login.html")
    except:
        return HttpResponse('<h1> server error</h1>')


@login_is_required
def Sign_out(request):
    try:
        request.session.clear()
        return  redirect('/')
    except:
        return HttpResponse('<h1> server error</h1>')
