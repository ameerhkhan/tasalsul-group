from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Products_all
from django.utils import timezone
import pandas as pd


# historical = []

hist_dict = {
    'DATE': [''],
    'NAME': '',
    'PRICE': ''
}

product = []
product_price = []
updating = []

@receiver(post_save, sender=Products_all)
def update_history(sender, instance, created, **kwargs):
    historical = []

    historical.append((instance.product_name, instance.product_price, instance.price_date))
    hist_dict['DATE'] = [instance.price_date.strftime("%x")]
    hist_dict['NAME'] = instance.product_name
    hist_dict['PRICE'] = instance.product_price

    df = pd.DataFrame(hist_dict).set_index('DATE')
    Products_all.product_price = timezone.now()

    # Create a new csv file with the headers already inplace for effective use. header = False will remove
    # HEADINGS i.e. DATE, NAME, PRICE
    # DATE CONVENTION --> MONTH, DAY, YEAR
    df.to_csv('pricing/assets/historical_pricing.csv', mode='a', header=False)

    backup_file = open('pricing/assets/backup.txt', 'a')
    backup_file.write("\n" + str(historical[0]))
    backup_file.close()