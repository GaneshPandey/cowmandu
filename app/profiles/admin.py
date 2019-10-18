from django.contrib import admin
from .models import ManagerProfile, CustomerProfile

admin.site.register(ManagerProfile)


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
