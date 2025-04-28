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

    name = models.CharField(max_length=100)
    status = models.CharField(choices=ContractStatus, default=ContractStatus.DRAFT)
    last_update = models.DateTimeField(default=now, editable=True)

    def __str__(self) -> str:
        return f"{self.name}"
