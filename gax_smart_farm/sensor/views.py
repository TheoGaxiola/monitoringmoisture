from django.shortcuts import render
from sensor.models import Node, Moisture
from rest_framework import viewsets
from rest_framework import permissions
from sensor.serializers import NodeSerializer, MoistureSerializer


class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class MoistureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Moisture.objects.all()
    serializer_class = MoistureSerializer
    permission_classes = [permissions.IsAuthenticated]
