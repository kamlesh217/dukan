from django.urls import path
from core_app.views import *


urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('contact/', contact),
    path('<str:group>/<int:id>/<str:category>/', sell_list),
    path('status/', Status),
    path('product/<int:item_id>/', detail , name="item_detail" ),
]