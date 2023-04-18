from django.contrib import admin
from materials.models import Material
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'quantity']

