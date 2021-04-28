from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=200)
    product_banner = models.FilePathField(path="/produce/images/")
    # Add field for product thumbnail
    product_thumbnail = models.FilePathField(path="/produce/images/")
    # Add video here..
    product_video = models.FilePathField("/produce/videos/", default="/produce/images/otherfv/apples.png")

    # Add video, quotation form, 6 types of packaging atleast.
    # for packaging make another class.. for all types of products.~

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

# add new class for product packaging options
class Product_packaging(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    packaging_picture = models.FilePathField(path="/produce/images/")
    packaging_name = models.CharField(max_length=30)

    def __str__(self):
        return self.packaging_name

# Add new class for salt X

class Salt(models.Model):
    salt_class = models.CharField(max_length=30)
    salt_description = models.CharField(max_length=200)
    salt_banner = models.FilePathField(path="/produce/images/")
    salt_thumbnail = models.FilePathField(path="/produce/images/")

    def __str__(self):
        return self.salt_type

class Salt_products(models.Model):
    salt = models.ForeignKey(Salt, on_delete=models.CASCADE)
    salt_type = models.CharField(max_length=30)
    salt_origin = models.CharField(max_length=20)
    salt_type_picture = models.FilePathField(path="/produce/images/")

# Add new class for meat
class Meat(models.Model):
    meat_animal = models.CharField(max_length=30)
    meat_description = models.CharField(max_length=200)
    meat_banner = models.FilePathField(path="/produce/images/")
    meat_thumbnail = models.FilePathField(path="/produce/images/")

    def __str__(self):
        return self.meat_animal

class Meat_products(models.Model):
    meat = models.ForeignKey(Meat, on_delete=models.CASCADE)
    meat_type = models.CharField(max_length=30)
    meat_type_picture = models.FilePathField(path="/produce/images/")


class Pulses(models.Model):
    pulses_name = models.CharField(max_length=30)
    pulses_description = models.CharField(max_length=200)
    pulses_banner = models.FilePathField(path="/produce/images/")
    pulses_thumbnail = models.FilePathField(path="/produce/images/")

    def __str__(self):
        return self.salt_type

class Pulses_products(models.Model):
    pulses = models.ForeignKey(Pulses, on_delete=models.CASCADE)
    pulses_type = models.CharField(max_length=30)
    pulses_type_picture = models.FilePathField(path="/produce/images/")

