from django.db import models

# Create your models here.


class Seller_order_table(models.Model):
    customer=models.ForeignKey("user_app.Custom_user", on_delete=models.CASCADE)
    order=models.ForeignKey("order_app.OrderItems", on_delete=models.CASCADE)
    is_complate=models.BooleanField()
    
    