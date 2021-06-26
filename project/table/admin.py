from django.contrib import admin
from . import models


@admin.register(models.Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ["id", "count", "consult_date", "product_url", "product_created_at"]
