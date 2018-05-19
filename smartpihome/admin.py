from django.contrib import admin
from .models import RaspberryPi, Light, RGBLight, DistanceSensor

class RaspberryPiAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
admin.site.register(RaspberryPi, RaspberryPiAdmin)

class LightAdmin(admin.ModelAdmin):
    list_display = ['name', 'pin', 'pi']
admin.site.register(Light, LightAdmin)

class RGBLightAdmin(admin.ModelAdmin):
    list_display = ['name', 'pinRed', 'pinGreen', 'pinBlue']
admin.site.register(RGBLight, RGBLightAdmin)

class DistanceSensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'trigger_pin', 'echo_pin', 'pi']
admin.site.register(DistanceSensor, DistanceSensorAdmin)


# Register your models here.
