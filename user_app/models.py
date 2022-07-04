from django.db import models



class Custom_user(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=models.CharField(max_length=50)
    password=models.TextField()
    is_admin=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)
    id_deleted=models.BooleanField(default=True)
    location=models.ForeignKey('product_app.Location_table',models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return self.first_name
    