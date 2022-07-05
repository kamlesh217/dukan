
from django.shortcuts import *
from cart_app.models import *
from product_app.models import *


def categories_processor(request):
    data=[]
    category_list=Category_group.objects.all()
    for item in category_list:
        data.append({"group":item.category_group_name, 'cat_list':Category.objects.filter(category_group=item)})
    return {'list':data}