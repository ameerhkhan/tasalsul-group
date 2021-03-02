from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=200)
    product_banner = models.FilePathField(path="/produce/images/")

    def __str__(self):
        return self.product_name
    

class Product_types(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=20)
    product_origin = models.CharField(max_length=30)
    product_grade = models.CharField(max_length=10)
    product_picture = models.FilePathField(path="/produce/images/")   # holds a string but must point to a file path name.


    def __str__(self):
        return self.product_type