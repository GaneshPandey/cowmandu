from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CUSTOMER = 'customer'
    MANAGER = 'manager'

    TYPE_CHOICES = (
        (CUSTOMER, 'Customer'),
        (MANAGER, 'Manager')
    )

    role = models.CharField(
        choices=TYPE_CHOICES,
        default=CUSTOMER,
        max_length=10
    )

    is_subscriber = models.BooleanField(default=False)

    @property
    def is_manager(self):
        return self.role == self.MANAGER

    @property
    def is_customer(self):
        return self.role == self.CUSTOMER

    def __str__(self):
        return self.get_username()
