from django.db import models
from django.utils import timezone
import pandas as pd

import datetime
# Create your models here.


class Products_all(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField(default=0)
    price_date = models.DateTimeField('updated on')
    product_picture = models.ImageField(upload_to='/images')
    product_picture2 = models.FilePathField(path='/images')

    def __str__(self):
        return self.product_name

    def was_updated_recently(self):
        return self.price_date >= timezone.now() - datetime.timedelta(days=1)