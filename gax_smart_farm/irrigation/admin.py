
from django.contrib import admin
from irrigation.models import Irrigation, Sector
from authentication.models import User
from sensor.models import Node, Moisture


admin.site.register(Irrigation)
admin.site.register(Sector)
admin.site.register(Node)
admin.site.register(Moisture)
admin.site.register(User)