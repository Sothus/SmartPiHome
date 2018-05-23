from channels import Group
from django.core.management import BaseCommand
from smartpihome.models import Light, RGBLight, RaspberryPi
import time, pigpio
from hardware.LED import LED
from hardware.RGB_LED import RGB_LED

class Command(BaseCommand):
	
	def handle(self, *args, **kwargs):
		pi_db = RaspberryPi.objects.all()
		pis = {}
		pi_connected = {}
		for pi in pi_db:
			pis[pi.name] = pigpio.pi(pi.address)
			
		
		#init LEDs
		db_lights = Light.objects.all()
		LEDs = {}
		for db_light in db_lights:
			if pis[db_light.pi.name].connected:
				LEDs[db_light.name] =  LED(pis[db_light.pi.name],
											db_light.pin)

		#init RGB_LEDs
		db_rgb_lights = RGBLight.objects.all()
		RGB_LEDs = {}
		for db_rgb_light in db_rgb_lights:
			if pis[db_rgb_light.pi.name].connected:
				RGB_LEDs[db_rgb_light.name] =  RGB_LED(db_rgb_light.pinRed,
														db_rgb_light.pinGreen,
														db_rgb_light.pinBlue,
														pi=pis[db_rgb_light.pi.name])

		while True:
			#handle LEDs
			lights = Light.objects.all()
			for light in lights:
				if pis[light.pi.name].connected:
					if light.is_on:
						LEDs[light.name].on()
					else:
						LEDs[light.name].off()
			
			#handle RGB LEDs
			rgb_lights = RGBLight.objects.all()
			for rgb_light in rgb_lights:
				if pis[rgb_light.pi.name].connected:
					if rgb_light.is_on:
						RGB_LEDs[rgb_light.name].on()
						RGB_LEDs[rgb_light.name].set_color(	red = rgb_light.colorRed,
														green = rgb_light.colorGreen,
														blue = rgb_light.colorBlue)
					else:
						RGB_LEDs[rgb_light.name].off()
					
			time.sleep(0.5)
			
			
def set_lights():
	lights = Light.objects.all()
	for light in lights:
		pi.set_mode(light.pin, pigpio.OUTPUT)
		pi.write(light.pin, light.is_on)

		
