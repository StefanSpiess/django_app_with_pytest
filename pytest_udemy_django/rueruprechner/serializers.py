"""Rest API Serializers for RuerupRechner"""

from rest_framework import serializers
from rueruprechner.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    """Serialize Contract model from database to JSON"""

    class Meta:
        """Metamodel definition for ContractSerializer"""

        model = Contract
        fields = ["id", "name", "status", "last_update"]
