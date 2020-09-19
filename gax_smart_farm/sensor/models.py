
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from irrigation.models import Sector

node_types = (
    ("valve", "Valvula"),
    ("moisture", "Humedad"),
    ("other", "Otra"),
)


class Node(models.Model):
    sector = models.ForeignKey(Sector, related_name="node", on_delete=models.CASCADE)
    identifier = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="node", on_delete=models.CASCADE)
    latitude = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, choices=node_types)

    class Meta:
        db_table = 'node'


class Moisture(models.Model):
    node = models.ForeignKey(Node, related_name="moisture", on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "moisture"
