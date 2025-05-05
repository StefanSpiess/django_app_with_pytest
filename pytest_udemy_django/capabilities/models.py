"""Module managing database models"""

from django.db import models
from django.utils.timezone import now


class Project(models.Model):
    """A specific ruerup contract

    A ruerup contract is a specific German variant
    of private rent system which is subsidized by
    the state and freezes the invested capital
    completely until you reach the age where you are
    entitled to receive rent payments.
    """

    class ProjectStatus(models.TextChoices):
        """The status of the contract

        Subject to review by the RuerupRechner Team.
        Only contracts that have been checked for
        integrity are added to the database."""

        NOT_STARTED = "Pending Confirmation"
        CONFIRMED = "Confirmed"
        ONGOING = "Ongoing"
        DONE = "Done"
    
    class ProjectKey(models.TextChoices):
        """The status of the contract

        Subject to review by the RuerupRechner Team.
        Only contracts that have been checked for
        integrity are added to the database."""
        
        DEFAULT = ""
        BMW = "BMW1302"
        SWM = "SWM0047"
        

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(choices=ProjectStatus, default=ProjectStatus.NOT_STARTED)
    project_key = models.CharField(choices=ProjectKey, default=ProjectKey.DEFAULT)
    last_update = models.DateTimeField(default=now, editable=True)
    objects = models.Manager()
    notes = models.TextField(verbose_name="Personal Notes", max_length=None, default="")

    def __str__(self) -> str:
        return f"{self.name}"