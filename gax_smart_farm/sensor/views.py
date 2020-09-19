from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from rest_framework import permissions

from sensor.models import Node, Moisture
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


class MoistureGeneralView(generic.ListView):
    template_name = 'sensor/moisture.html'
    context_object_name = 'latest_moisture_list'

    def get_queryset(self):
        return Moisture.objects.all()
