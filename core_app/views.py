from tkinter.tix import Tree
from urllib import response
from django.shortcuts import render,redirect
from cart_app.models import Cart_table
from product_app.models import Product_table
from review_app.models import Reviews
from review_app.views import add_rating_to_product
from django.http import JsonResponse
from django.db.models import Q

from user_app.dec import login_is_required

# Create your views here.
def Dashboard(request):
    context={'latest':Product_table.objects.filter(is_deleted=False).reverse()[:8]}
    return render(request, 'index.html',context)

def contact(request):
    return render(request, "contact.html")

def category_sell_list(request, group, id, category):
    data={'products':Product_table.objects.filter(category=id,is_deleted=False),
    'path':f"Product: {group}/ {category}"}
    return render(request, 'shop.html', data)

def group_sell_list(request, group):
    data={'products':Product_table.objects.filter(category__category_group__category_group_name=group,is_deleted=False ),
    'path':f"Product: {group}"}
    return render(request, 'shop.html', data)


def detail(request, item_id):
    context={"product":Product_table.objects.filter(id=item_id)[0],
    "review":Reviews.objects.filter(product_id=item_id).reverse()[:10],
    'list':Product_table.objects.filter(category=(Product_table.objects.filter(id=item_id)[0]).category)}

    if request.method=="POST":
        message=request.POST["massage"]
        rating=request.POST['RadioOptions']
        name=request.POST['name']
        email=request.POST['email']
        review=Reviews.objects.create(review=message, rating=rating, name=name,email=email,product_id=item_id)
        review.save()
        add_rating_to_product(item_id)
        return redirect(f'/product/{item_id}')
    if Product_table.objects.filter(id=item_id)[0].is_deleted:
        context['is_deleted']=True
        return render(request, "detail.html", context)
    else:
        return render(request, "detail.html", context)


def search(request):
    if request.method=='GET':
        value=request.GET.get('search_value')
        if not value=="": 
            search_list=Q(product_name__icontains=value) | Q(tags__icontains=value) | Q(brand__icontains=value) | Q(product_desc__icontains=value) | Q(category__category_name__icontains=value) | Q(category__category_group__category_group_name__icontains=value)
            data={'products':Product_table.objects.filter(search_list,is_deleted=False).distinct(),
            'path':f"Product: {value}"}
            return render(request, 'shop.html', data)
        else:
            data={'path':f"Product: {value}"}
            return render(request, 'shop.html', data)