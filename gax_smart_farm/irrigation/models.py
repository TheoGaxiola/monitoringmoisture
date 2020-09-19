from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Sector(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sector", on_delete=models.CASCADE,)

    class Meta:
        db_table = "sector"


class Irrigation(models.Model):
    sector = models.ForeignKey(Sector, related_name="irrigation", on_delete=models.CASCADE)
    sector_valves = JSONField()
    time = models.IntegerField()
    valves_data = JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="irrigation", on_delete=models.CASCADE,)
    stopped_manually = models.BooleanField(default=False)
    is_executed = models.BooleanField(default=False)

    class Meta:
        db_table = "irrigation"
