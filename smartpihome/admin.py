from django.contrib import admin
from .models import RaspberryPi, Light, RGBLight, TemperatureSensor, GPA


class RaspberryPiAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
admin.site.register(RaspberryPi, RaspberryPiAdmin)


class LightAdmin(admin.ModelAdmin):
    list_display = ['name', 'pin', 'is_on','pi']
admin.site.register(Light, LightAdmin)


class RGBLightAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_on', 'pinRed', 'pinGreen', 'pinBlue', "colorRed", "colorGreen", "colorBlue"]
admin.site.register(RGBLight, RGBLightAdmin)


class TemperatureSensorAdmin(admin.ModelAdmin):
	list_display = ['name', 'sensor_id']
admin.site.register(TemperatureSensor, TemperatureSensorAdmin)


class GPAAdmin(admin.ModelAdmin):
	list_display = ['name', 'pi']
admin.site.register(GPA, GPAAdmin)

