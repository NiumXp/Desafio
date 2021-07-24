import os

from django.db import transaction

from ..models import Field

path = os.path.dirname(__file__)
path = os.path.join(path, "raw.json")

with open(path) as fp:
    data = fp.read()
    data = data.replace("<UTC>", "timezone.utc")

    import datetime
    from django.utils import timezone
    data = eval(data)


@transaction.atomic
def insert():
    for d in data:
        kwargs = {}

        kwargs["count"]              = d['c']
        kwargs["consult_date"]       = d["consult_date"]
        kwargs["store_url"]          = d["store_url"]
        kwargs["product_url"]        = d["product_url"]
        kwargs["product_url_image"]  = d["product_url__image"]
        kwargs["product_created_at"] = d["product_url__created_at"]

        field = Field(**kwargs)
        field.save()
