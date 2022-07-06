from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist , name="wishlist"  ),
    path('wish_to_cart/<int:item_id>/', views.wish_to_cart, name="wishlist_to_cart"  ),
    path('remove_wish/<int:item_id>/', views.delect_from_wishlist , name="delect_from_wishlist"  ),
]