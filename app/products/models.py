from django.db import models
from materials.models import Material

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='files/images/products', null=True, blank=True)

    description = models.TextField()
    quantity = models.IntegerField()

    materials = models.ManyToManyField(Material, blank=True)
