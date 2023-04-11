from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    WORKER = 'worker'
    CUSTOMER = 'customer'
    ADMIN = 'admin'

    roles_choises = (
        (WORKER, WORKER),
        (CUSTOMER, CUSTOMER),
        (ADMIN, ADMIN)
    )

    roles = models.CharField(max_length=255, choices=roles_choises, default=CUSTOMER)
    tel_number = models.CharField(max_length=15, blank=True, null=True)
