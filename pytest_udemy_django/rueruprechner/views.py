"""To view or not to view?"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rueruprechner.serializers import (
    ContractSerializer,
    VendorSerializer,
    VendorProposal,
)
from rueruprechner.models import Contract, Vendor


class ContractViewSet(ModelViewSet):
    "ModeViewSet for ruerup Contract model"

    serializer_class = ContractSerializer
    queryset = Contract.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


class VendorViewSet(ModelViewSet):
    "ModeViewSet for ruerup Vendor model"

    serializer_class = VendorSerializer
    queryset = Vendor.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


class VendorProposalViewSet(ModelViewSet):
    "ModeViewSet for ruerup Vendor model"

    serializer_class = VendorProposal
    queryset = VendorProposal.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
