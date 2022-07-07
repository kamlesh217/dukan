from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages
from requests import request
from django.http import JsonResponse


def seller_logout_is_required(function=None):
    def wrap(request,*args, **kwargs):
        if not request.session.get('seller_is_active', False):
            return function(request,*args, **kwargs)
        else:
            return redirect('/seller')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def seller_login_is_required(function=None):
    def wrap(request,*args, **kwargs):
        if  request.method=="GET":
            if not request.GET.get('is_ajax'):
                if request.session.get('seller_is_active', False):
                    return function(request,*args, **kwargs)
                else:
                    request.session.clear()
                    messages.success(request, 'You should be logged in before open that')
                    return redirect('/seller/sign_in_user')
            else:
                if request.session.get('seller_is_active', False):
                    return function(request,*args, **kwargs)
                else:
                    request.session.clear()
                    messages.success(request, 'You should be logged in before open that')
                    return JsonResponse({'success':True,'login_req':True})
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap