from tkinter.tix import Tree
from django.shortcuts import render

from user_app.dec import login_is_required

# Create your views here.
def Dashboard(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, "contact.html")