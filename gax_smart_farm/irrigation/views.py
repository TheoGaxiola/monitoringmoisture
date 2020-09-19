from django.shortcuts import render
from irrigation.models import Sector, Irrigation
from rest_framework import viewsets
from rest_framework import permissions
from irrigation.serializers import SectorSerializer, IrrigationSerializer


class SectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [permissions.IsAuthenticated]


class IrrigationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Irrigation.objects.all()
    serializer_class = IrrigationSerializer
    permission_classes = [permissions.IsAuthenticated]