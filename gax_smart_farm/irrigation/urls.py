
from django.urls import include, path
from rest_framework import routers
from irrigation import views


app_name = "irrigation"

router = routers.DefaultRouter()
router.register(r"irrigation", views.IrrigationViewSet, basename="irrigation")
router.register(r"sector", views.SectorViewSet, basename="sector")

urlpatterns = [path("", include(router.urls))]

