from django.urls import path
from .views import *


urlpatterns = [
    path('', Seller_dashboard),
    path('sign_out_user/', Sign_out_seller),
    path('sign_in_user/', Sign_in_seller),
    path('sign_up_user/', Sign_up_seller),
    path('order_list', Order_list),
    path('add_new', Add_new_product),
]