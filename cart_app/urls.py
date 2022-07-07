from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart , name="cart"  ),
    path('add_to_cart/<int:item_id>/',views.add_new_cart ),
    path('cart_to_wish/<int:item_id>/', views.cart_to_wishlist, name="add_to_wishlist"  ),
    path('remove_cart/<int:item_id>/', views.delect_from_cart, name="delect_from_cart"  ),
    path('remove_one_cart/<int:item_id>/',views.remove_one_cart),
    path('add_one_cart/<int:item_id>/',views.add_one_cart),
    
    
]