from django.shortcuts import render
from .models import RGBLight, Light, TemperatureSensor


def light_page(request):
	lights = Light.objects.all()
	rgbLights = RGBLight.objects.all()
	
	return render(	request,
					'light.html',
					{
						"lights": lights,
						"rgbLights": rgbLights,
					})


def temperature_page(request):
	temperature_sensors = TemperatureSensor.objects.all()
	return render(	request, 
					'temperature.html',
					{
						"temps": temperature_sensors,
					})
					

def sensor_page(request):
	return render(request, 'sensor.html')
