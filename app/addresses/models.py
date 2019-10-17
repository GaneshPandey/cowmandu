from django.db import models
from django.conf import settings


KATHMANDU = 'kathmandu'
BHAKTAPUR = 'bhaktapur'
LALITPUR = 'lalitpur'

CITY_CHOICES = (
    (KATHMANDU, 'Kathmandu'),
    (BHAKTAPUR, 'Bhaktapur'),
    (LALITPUR, 'Lalitpur'),
)


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    address_line_1 = models.CharField(
        max_length=125,
        blank=True,
        null=True
    )
    address_line_2 = models.CharField(
        max_length=125,
        blank=True,
        null=True
    )
    city = models.CharField(
        choices=CITY_CHOICES,
        default=KATHMANDU,
        max_length=20,
    )
    nearby_location = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    latitude = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    longitude = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    @property
    def get_full_address(self):
        return f"" \
            f"{self.address_line_1}\n" \
            f"{self.address_line_2}\n" \
            f"{self.city}"

    def __str__(self):
        return f"{self.user.username}-{self.city}"