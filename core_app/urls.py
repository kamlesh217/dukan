from django.urls import path
from core_app.views import *


urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('contact/', contact),
]