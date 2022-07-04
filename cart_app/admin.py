from django.contrib import admin

from cart_app.models import Cart_table, Wishlist_table

# Register your models here.

admin.site.register(Cart_table)
admin.site.register(Wishlist_table)