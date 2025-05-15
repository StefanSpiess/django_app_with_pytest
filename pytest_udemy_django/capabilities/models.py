"""Module managing database models"""

from django.db import models
from django.utils.timezone import now


class Project(models.Model):
    """A Project
    
    """

    class ProjectStatus(models.TextChoices):
        """Possible status values
        
        """

        NOT_STARTED = "Pending Confirmation"
        CONFIRMED = "Confirmed"
        ONGOING = "Ongoing"
        DONE = "Done"

    class ProjectKey(models.TextChoices):
        """Available Project Keys
        
        """

        UNDEFINED = "TBD", "TBD"
        BMW = "BMW1302", "BMW1302"
        SWM = "SWM0047", "SWM0047"

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(choices=ProjectStatus, default=ProjectStatus.NOT_STARTED)
    project_key = models.CharField(choices=ProjectKey, default=ProjectKey.UNDEFINED)
    last_update = models.DateTimeField(default=now, editable=True)
    objects = models.Manager()
    notes = models.TextField(verbose_name="Personal Notes", max_length=None, default="")

    def __str__(self) -> str:
        return f"{self.name}"
