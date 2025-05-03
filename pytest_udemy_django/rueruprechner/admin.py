"""Register your models here"""

from django.contrib import admin
from rueruprechner.models import Contract, Vendor


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Ruerup Contract Admin Model"""

    pass


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """Ruerup Vendor Admin Model"""

    pass
