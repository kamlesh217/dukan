from django.db import models

# Create your models here.
class Wishlist_table(models.Model):
    product=models.ForeignKey('product_app.Product_table', on_delete=models.CASCADE)
    customer=models.ForeignKey('user_app.Custom_user', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.customer.first_name