from django.contrib import admin

from order_app.models import OrderDetails, OrderItems

# Register your models here.
admin.site.register(OrderDetails)
admin.site.register(OrderItems)