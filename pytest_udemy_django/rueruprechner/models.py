"""Module managing database models"""

from django.db import models
from django.utils.timezone import now


class Contract(models.Model):
    """A specific ruerup contract

    A ruerup contract is a specific German variant
    of private rent system which is subsidized by
    the state and freezes the invested capital
    completely until you reach the age where you are
    entitled to receive rent payments.
    """

    class ContractStatus(models.TextChoices):
        """The status of the contract

        Subject to review by the RuerupRechner Team.
        Only contracts that have been checked for
        integrity are added to the database."""

        DRAFT = "Draft"
        PENDING_REVIEW = "Pending Review"
        CONFIRMED = "Confirmed"

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(choices=ContractStatus, default=ContractStatus.DRAFT)
    last_update = models.DateTimeField(default=now, editable=True)
    objects = models.Manager()
    notes = models.TextField(verbose_name="Personal Notes", max_length=None, default="")

    def __str__(self) -> str:
        return f"{self.name}"


class Vendor(models.Model):
    """A specific vendor of ruerup products

    These are vile companies that try to talk people
    into signing ruerup contract to buy their products."""

    class VendorCategory(models.TextChoices):
        """The class of a vendor

        Roughly speaking: this is the categorization
        of the vileness of a vendor. In realitiy,
        vileness is obviously located on a seamlessly
        scaling continuum."""

        UNKNOWN = "Unknown"
        MOSTLY_HONEST = "Mostly honest"
        PRETTY_VILE = "Pretty vile"
        PURE_EVIL = "Pure evil"

    name = models.CharField(max_length=120, unique=True)
    vileness = models.CharField(choices=VendorCategory, default=VendorCategory.UNKNOWN)
    last_update = models.DateTimeField(default=now, editable=True)
    objects = models.Manager()
    notes = models.TextField(verbose_name="Personal Notes", max_length=None, default="")


class VendorProposal(Vendor):
    """A proposal for a new vendor by a user

    These should later be easily transformable
    to a Vendor Class object. I would not usually
    implement this feature the way I did (via
    e-mail) but for the sake of the udemy course
    I did so."""

    class VendorProposalStatus(models.TextChoices):
        """Status choice for a VendorProposal"""

        NEW = "New"
        ACCEPTED = "Accepted"
        REJECTED = "Rejected"

    proposal_status = models.CharField(
        choices=VendorProposalStatus, default=VendorProposalStatus.NEW, editable=False
    )
