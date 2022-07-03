from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages

def logout_is_required(function=None):

    def wrap(request):
        if not request.session.get('is_active', False):
            return function(request)
        else:
            return redirect('/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def login_is_required(function=None):
    def wrap(request):
        if request.session.get('is_active', False):
            return function(request)
        else:
            request.session.clear()
            messages.success(request, 'You should be logged in before open that')
            return redirect('/user/sign_in_user')
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap