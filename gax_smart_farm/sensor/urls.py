
from django.urls import include, path
from rest_framework import routers
from sensor import views


app_name = "sensor"

router = routers.DefaultRouter()
router.register(r"node", views.NodeViewSet, basename="node")
router.register(r"moisture", views.MoistureViewSet, basename="moisture")

urlpatterns = [path("", include(router.urls))]

