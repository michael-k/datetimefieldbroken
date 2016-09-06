from django.db import models
from django.utils import timezone


class Dummy(models.Model):
    dt_with_default = models.DateTimeField(default=timezone.now)
    dt_without_default = models.DateTimeField()
