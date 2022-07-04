from tkinter.tix import Tree
from django.shortcuts import render
from product_app.models import Product_table
from review_app.models import Reviews
from review_app.views import add_rating_to_product

from user_app.dec import login_is_required

# Create your views here.
def Dashboard(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, "contact.html")

def sell_list(request):
    product=Product_table.objects.all()
    return render(request, 'shop.html', {'products':product})

def detail(request, item_id):
    context={"product":Product_table.objects.get(id=item_id)}
    if request.method=="POST":
        massage=request.POST["massage"]
        rating=request.POST['RadioOptions']
        name=request.POST['name']
        email=request.POST['email']
        review=Reviews.objects.create(review=massage, rating=rating, name=name,email=email,product_id=item_id)
        review.save()
        add_rating_to_product(item_id)        
        
    return render(request, "detail.html", context)