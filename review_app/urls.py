from django.urls import path
from .views import *


urlpatterns = [
    path('<int:id>/',all_reviews ),
]