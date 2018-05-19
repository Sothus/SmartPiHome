from channels import Group
from django.core.management import BaseCommand
from smartpihome.models import Light, RaspberryPi
import time, pigpio

class Command(BaseCommand):
	
	def handle(self, *args, **kwargs):
		pi_db = RaspberryPi.objects.all()
		pis = {}
		pi_connected = {}
		for pi in pi_db:
			pis[pi.name] = pigpio.pi(pi.address)
			

		while True:
			lights = Light.objects.all()
			for light in lights:
				if pis[light.pi.name].connected:
					pis[light.pi.name].set_mode(light.pin, pigpio.OUTPUT)
					pis[light.pi.name].write(light.pin, light.is_on)
			time.sleep(1)
			
			
def set_lights():
	lights = Light.objects.all()
	for light in lights:
		pi.set_mode(light.pin, pigpio.OUTPUT)
		pi.write(light.pin, light.is_on)

		
