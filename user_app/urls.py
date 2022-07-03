from django.urls import path
from user_app.views import *


urlpatterns = [
    path('sign_out_user/', Sign_out),
    path('sign_in_user/', Sign_in),
    path('sign_up_user/', Sign_up)
]