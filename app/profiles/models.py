from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


MALE = 'male'
FEMALE = 'female'
OTHER = 'other'

GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
)


class ManagerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='manager_profile',
        verbose_name=_('user'),
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(null=True, blank=True)
    phone_no = models.CharField(
        max_length=10
    )
    profile_photo = models.ImageField(
        upload_to='profile',
        default='profile/profile_default.png',
        blank=True
    )
    cover_photo = models.ImageField(
        upload_to='profile/cover-image',
        default='profile/cover-image/cover_default.jpg',
        blank=True
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=OTHER,
        max_length=6
    )

    def __str__(self):
        return self.user.username


class CustomerProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='customer_profile',
        verbose_name=_('user'),
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(null=True, blank=True)
    phone_no = models.CharField(
        max_length=10
    )
    profile_photo = models.ImageField(
        upload_to='profile',
        default='profile/profile_default.png',
        blank=True
    )
    cover_photo = models.ImageField(
        upload_to='profile/cover-image',
        default='profile/cover-image/cover_default.jpg',
        blank=True
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=OTHER,
        max_length=6
    )

    def __str__(self):
        return self.user.username
