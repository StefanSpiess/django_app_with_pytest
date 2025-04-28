"""We want to route it route it!"""

from rest_framework import routers
from .views import ContractViewSet

contract_router = routers.DefaultRouter()
contract_router.register(
    prefix="contracts", viewset=ContractViewSet, basename="contracts"
)
