from django.db import models

# Create your models here.
class Reviews(models.Model):
    product=models.ForeignKey('product_app.Product_table',on_delete=models.CASCADE)
    email=models.CharField(max_length=50)
    name=models.CharField( max_length=50)
    rating=models.IntegerField(default=0)
    review=models.TextField()
    comment=models.CharField( max_length=200)
    date=models.DateField( auto_now_add=True)
    time=models.TimeField( auto_now_add=True)
    helpfull=models.IntegerField(default=0)

    class Meta:
        ordering=['time']

    def __str__(self):
        return self.product.product_name