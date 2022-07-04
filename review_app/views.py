from django.shortcuts import render,redirect
from product_app.models import Product_table

from review_app.models import Reviews

# Create your views here.
def all_reviews(request, id):
    review_list=Reviews.objects.filter(product_id=id).reverse()
    context={
        "review":review_list,
        "rat_list":rating_(id),
        'product':Product_table.objects.get(id=id)
    }
    return render(request, "review.html", context )

def rating_(id):
    if Reviews.objects.filter(product_id=id).count()==0:
        rat_list=[0,0,0,0,0]
        return rat_list
    else:
        total=Reviews.objects.filter(product_id=id).count()
        rat_list=[]
        a=0
        for i in range(1,6):
            rat=Reviews.objects.filter(product_id=id,rating=i).count()
            a+=rat*i
            value=rat*100/total
            value=round(value,2)
            rat_list.append(value)
        rat_list.append(str(a/total)[:3])

        return rat_list

def helpfull(request,review_id):
    review=Reviews.objects.get(id=review_id)
    review.helpfull+=1
    review.save()
    product_id=Reviews.object.get(id=review_id)
    return redirect('')

def add_rating_to_product(id):
    rev=Reviews.objects.filter(product_id=id).count()
    a=0
    for i in range(1,6):
        rat=Reviews.objects.filter(product_id=id,rating=i).count()
        a+=rat*i
    rat=str(a/rev)[:3]

    item=Product_table.objects.get(id=id)
    item.review_count=rev
    item.rating_count=rat
    item.save()