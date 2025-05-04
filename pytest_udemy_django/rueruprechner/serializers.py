"""Rest API Serializers for RuerupRechner"""

from rest_framework import serializers
from rueruprechner.models import Contract, Vendor, VendorProposal


class ContractSerializer(serializers.ModelSerializer):
    """Serialize Contract model from database to JSON"""

    class Meta:
        """Metamodel definition for ContractSerializer"""

        model = Contract
        fields = ["id", "name", "status", "last_update", "notes"]


class VendorSerializer(serializers.ModelSerializer):
    """Serialize Vendor model from database to JSON"""

    class Meta:
        """Metamodel definition for VendorSerializer"""

        model = Vendor
        fields = ["id", "name", "vileness", "last_update", "notes"]


class VendorSerializer(serializers.ModelSerializer):
    """Serialize VendorProposal model from database to JSON"""

    class Meta:
        """Metamodel definition for VendorProposalSerializer"""

        model = VendorProposal
        fields = ["id", "name", "vileness", "last_update", "notes", "proposal_status"]
