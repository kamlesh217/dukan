from pickletools import decimalnl_short
from statistics import mode
from django.db import models




# Create your models here.
class Location_table(models.Model):
    address_line1=models.CharField(max_length=50)
    address_line2=models.CharField(max_length=50, null=True)
    city=models.CharField( max_length=30)
    state=models.CharField( max_length=30)
    district=models.CharField(max_length=30)
    postal_code=models.CharField( max_length=20)
    location_type=models.CharField(max_length=50, null=True)
    desc=models.TextField(null=True)


category_group_list=[
    ("Mobiles & Tablets", "Mobiles & Tablets"),
    ("Computers & laptops", "Computers & laptops"),
    ("Cameras", "Cameras"),
    ("Television", "Television"),
    ("Computer Peripherals", "Computer Peripherals"),
    ("Audio", "Audio"),
]

class Category_group(models.Model):
    category_group_name=models.CharField(choices=category_group_list, max_length=30)
    is_deleted=models.BooleanField(default=False)
    
    def __str__(self):
        return self.category_group_name

class Category(models.Model):
    category_group=models.ForeignKey(Category_group, on_delete=models.CASCADE)
    category_name=models.CharField( max_length=30)
    is_deleted=models.BooleanField(default=False)
    
    def __str__(self):
        return self.category_name
    
class Product_table(models.Model):
    product_name=models.CharField(max_length=100)
    product_desc=models.TextField( null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,null=True)
    list_price=models.DecimalField(max_digits=7, decimal_places=2)
    supplier=models.ForeignKey('user_app.Custom_user',models.SET_NULL,blank=True,null=True)
    min_price=models.DecimalField(max_digits=7, decimal_places=2)
    price_currency=models.CharField( max_length=15)
    display_image=models.ImageField( upload_to='product_image/')
    is_deleted=models.BooleanField(default=False)
    review_count=models.IntegerField(default=0)
    rating_count=models.FloatField(default=0)
    brand=models.CharField( max_length=50,default='')
    tags=models.TextField(null=True,default='')
    def __str__(self):
        return self.product_name 
    
class Warehouse(models.Model):
    warehouse_name=models.CharField(max_length=30)
    location_id=models.ForeignKey(Location_table,models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return self.warehouse_name

class Inventory(models.Model):
    product_id=models.ForeignKey(Product_table,models.SET_NULL,blank=True,null=True)
    warehouse_id=models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    Qty_in_hand=models.IntegerField(default=0, null=True)
    Qty_available=models.IntegerField(default=0, null=True)
    
    def __str__(self):
        return self.warehouse_id.warehouse_name
    
    


