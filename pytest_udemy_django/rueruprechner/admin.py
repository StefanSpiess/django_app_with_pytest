"""Register your models here"""

from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Ruerup Contract Admin Model"""

    pass
