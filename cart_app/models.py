from django.db import models

# Create your models here.

class Cart_table(models.Model):
    product=models.ForeignKey('product_app.Product_table',on_delete=models.CASCADE)
    customer=models.ForeignKey('user_app.Custom_user', on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.customer.first_name
    
    def get_total(self):
        return self.qty* self.product.min_price

