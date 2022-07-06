
from django.shortcuts import *
from cart_app.models import *
from product_app.models import *
from wishlist_app.models import Wishlist_table


def categories_processor(request):
    user=request.session.get('user',False)
    if user:
        request.session['cart_count']=Cart_table.objects.filter(customer_id=user).count()
        request.session['wishlist_count']=Wishlist_table.objects.filter(customer_id=user).count()
    data=[]
    category_list=Category_group.objects.all()
    for item in category_list:
        data.append({"group":item.category_group_name, 'cat_list':Category.objects.filter(category_group=item)})
    return {'list':data}