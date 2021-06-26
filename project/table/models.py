from django.db import models


class Field(models.Model):
    count = models.IntegerField()
    consult_date = models.DateField()
    store_url = models.CharField(max_length=1000)

    product_url = models.CharField(max_length=1000)
    product_url_image = models.CharField(max_length=1000)
    product_created_at = models.DateTimeField()
