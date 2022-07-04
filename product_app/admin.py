from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Location_table)
admin.site.register(Category_group)
admin.site.register(Category)
admin.site.register(Product_table)
admin.site.register(Warehouse)
admin.site.register(Inventory)