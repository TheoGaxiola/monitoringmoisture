from rest_framework import serializers
from sensor.models import Node, Moisture


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"


class MoistureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moisture
        fields = "__all__"
