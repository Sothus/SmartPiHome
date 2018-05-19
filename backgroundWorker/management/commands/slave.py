from channels import Group
from django.core.management import BaseCommand
from smartpihome.models import Light, RaspberryPi
import time, pigpio

class Command(BaseCommand):
	
	def handle(self, *args, **kwargs):
		pi_db = RaspberryPi.objects.filter(pk=1)
		pi = pigpio.pi(pi_db[0].address)
		lights = Light.objects.all()
		for light in lights:
			pi.set_mode(light.pin, pigpio.OUTPUT)
			
		while True:
			lights = Light.objects.all()
			for light in lights:
				pi.write(light.pin, light.is_on)
			time.sleep(1)
		
