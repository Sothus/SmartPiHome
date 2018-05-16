from channels import Group
from .models import RaspberryPi, Light, RGBLight, DistanceSensor

def ws_connect(message):
	print("Someone connected")

	
def ws_message(message):
	print("Received!" + message['text'])
	
def ws_disconnect(message):
	print("Someone left us")
