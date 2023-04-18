from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='files/images/materials', null=True, blank=True)

    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name