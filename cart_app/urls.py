from django.urls import path
from . import views



urlpatterns = [
    path('', views.cart , name="cart"  ),
    path('add_to_cart/<int:item_id>/',views.add_one_cart )
]