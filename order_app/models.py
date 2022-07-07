from django.db import models

# Create your models here.

class OrderDetails(models.Model):
    name=models.CharField(max_length=50)
    customer=models.IntegerField()
    phone=models.CharField( max_length=50)
    address=models.TextField()
    city=models.CharField( max_length=50)
    zipcode=models.CharField(max_length=50)
    state=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    total=models.FloatField()
    orderNo=models.IntegerField()
    billdate=models.DateField(auto_now_add=True)
    deliveryDate=models.DateField(null=True)
    
    
    def __str__(self):
        return f"name: {self.name} on {self.billdate} to {self.city}"
    

class OrderItems(models.Model):
    qty=models.IntegerField()
    totalPrice=models.FloatField()
    productID=models.ForeignKey('product_app.Product_table',on_delete=models.CASCADE)
    order=models.ForeignKey(OrderDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.name
    
    def has_delete_permission(self, request, obj=None):
        return False