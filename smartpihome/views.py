from django.shortcuts import render
from .models import RGBLight, Light

def home_page(request):
	return render(request, 'home.html')

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
	return render(request, 'temperature.html')

def sensor_page(request):
	return render(request, 'sensor.html')

def statistic_page(request):
	return render(request, 'statistic.html')

def about_page(request):
	return render(request, 'about.html')

# Create your views here.
