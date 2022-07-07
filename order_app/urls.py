from django.urls import path
from .views import *

urlpatterns = [
    path("", orders),
    path('checkout/', checkout)
]