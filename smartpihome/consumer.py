from channels import Group
from .models import RaspberryPi, Light, RGBLight, DistanceSensor
import json

def ws_connect(message):
	group_name = get_group(message)
	Group(group_name).add(message.reply_channel)
	
	print("Someone connected to " + group_name)
	
	message.reply_channel.send({
		"text": "You're connected to " + group_name + " group",
	})

	
def ws_message(message):
	print("Received!" + message['text'])
	
	group_name = get_group(message)
	
	if group_name == "light":
		dict_message = json.loads(message['text'])
		if "light" in dict_message:
			led = Light.objects.filter(name=dict_message['light'], pi__name=dict_message['raspberry'])
			if led:
				led = led[0]
			else:
				return None
				
			print(led)
			if led.is_on:
				print(led.is_on)
				led.is_on = False
			else:
				led.is_on = True	
			led.save()
			
		if "rgb_light" in dict_message:
			rgb_led = RGBLight.objects.filter(name=dict_message['rgb_light'], pi__name=dict_message['raspberry'])
			if rgb_led:
				rgb_led = rgb_led[0]
			else:
				return None
				
			print(rgb_led)
			if rgb_led.is_on:
				print(rgb_led.is_on)
				rgb_led.is_on = False
			else:
				rgb_led.is_on = True	
			rgb_led.save()
			
			
		if "rgb_light_set" in dict_message:
			rgb_led = RGBLight.objects.filter(name=dict_message['rgb_light_set'], pi__name=dict_message['raspberry'])
			if rgb_led:
				rgb_led = rgb_led[0]
			else:
				return None
				
			print(rgb_led)
			rgb_led.colorRed = dict_message['red_val']
			rgb_led.colorGreen = dict_message['green_val']
			rgb_led.colorBlue = dict_message['blue_val']
			
			rgb_led.save()

	elif group_name == "temperature":
		pass
	
def ws_disconnect(message):
	group_name = get_group(message)
	print("Someone left us form " + group_name + " group")
	Group(group_name).discard(message.reply_channel)
	
def get_group(message):
	message_path = message['path']
	splitted_path = message_path.split('/')
	group_name = splitted_path[1]

	return group_name
