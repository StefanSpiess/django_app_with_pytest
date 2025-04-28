"""To view or not to view?"""

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import ContractSerializer
from .models import Contract


class ContractViewSet(ModelViewSet):
    "ModeViewSet for ruerup Contract model"

    serializer_class = ContractSerializer
    queryset = Contract.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
