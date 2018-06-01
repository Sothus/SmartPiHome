from channels import Group
from django.core.management import BaseCommand
from smartpihome.models import Light, RGBLight, RaspberryPi, TemperatureSensor, GPA
import time, pigpio
from hardware.LED import LED
from hardware.RGB_LED import RGB_LED
from gpa.GPA import GarageParkingAssistant
from thermometer_handler.ThermometerHandler import ThermometerHandler
import json
import _thread

class Command(BaseCommand):
	
	def handle(self, *args, **kwargs):
		pi_db = RaspberryPi.objects.all()
		pis = {}
		pi_connected = {}
		for pi in pi_db:
			pis[pi.name] = pigpio.pi(pi.address)
		
		#init GPA
		db_gpas = GPA.objects.all()
		gpas = {}
		for db_gpa in db_gpas:
			if pis[db_gpa.pi.name].connected:
				gpas[db_gpa.pi.name] = GarageParkingAssistant(db_gpa.pi.address, db_gpa.pinTrig, db_gpa.pinEcho, db_gpa.pinLed1, db_gpa.pinLed2, db_gpa.pinLed3, db_gpa.pinLed4, db_gpa.pinBuzz)
				

		for gpa in gpas:
			print("elo")
			_thread.start_new_thread(gpas[gpa].start, ())
		
		print("wyszedlem")
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
														
		#init tempSensors
		db_temp_sens = TemperatureSensor.objects.all()
		TempSens = {}
		for db_temp_sen in db_temp_sens:
			TempSens[db_temp_sen.name] = ThermometerHandler(db_temp_sen.sensor_id)
			
		print(TempSens)

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
					
			#handle Temp Sensor
			sens = TemperatureSensor.objects.all()
			for sen in sens:
				temp = TempSens[sen.name].get_temperature_celsius()
				print(temp)
				group_message = json.dumps({"sensor_id" : str(sen.sensor_id), "value": str(temp), "sensor_name" : str(sen.name)})
				Group("temperature").send({"text" : group_message})
			time.sleep(0.5)
			
			

		
