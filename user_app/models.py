from django.db import models

# Create your models here.

class Custom_user(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=models.CharField(max_length=50)
    password=models.TextField()
    is_admin=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)


    def __str__(self):
        return self.first_name
    