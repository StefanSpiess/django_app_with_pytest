"""We want to route it route it!"""

from rest_framework import routers
from rueruprechner.views import ContractViewSet, VendorViewSet

my_router = routers.DefaultRouter()

my_router.register(
    prefix="contracts",
    viewset=ContractViewSet,
    basename="contracts",
)

my_router.register(
    prefix="vendors",
    viewset=VendorViewSet,
    basename="vendors",
)
