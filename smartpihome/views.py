from django.shortcuts import render, redirect
from .models import RGBLight, Light, TemperatureSensor, HumiditySensor


def home_page(request):
	return redirect('light/', request)

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
	humidity_sensors = HumiditySensor.objects.all()
	return render(	request, 
					'sensor.html',
					{
						"hums": humidity_sensors,
					})
