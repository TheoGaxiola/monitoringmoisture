from rest_framework import serializers
from irrigation.models import Sector, Irrigation


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = "__all__"


class IrrigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Irrigation
        fields = "__all__"
