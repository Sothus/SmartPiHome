'''IF YOU WANT TO RUN THIS SCRIPT, YOU SHOULD DO THIS FROM PARENT DIRECTORY'''

import pigpio, time, signal
from hardware.UltrasonicSensor import UltrasonicSensor
from hardware.LED import LED

class GarageParkingAssistant:


	def __init__(self, pi, trig, echo, led1, led2, led3, led4, buzz):
		self.pi = pigpio.pi(pi)
		self.sens = UltrasonicSensor(self.pi, trig, echo)
		self.led1 = LED(self.pi, led1)
		self.led2 = LED(self.pi, led2)
		self.led3 = LED(self.pi, led3)
		self.led4 = LED(self.pi, led4)
		self.buzz = buzz

		self.cleaner = SignalHandler()



	def start(self):
		self._running = True
		self._stopped = False
		while(self.cleaner.can_run() == True):

			distance = self.sens.read()

			if(distance < 80):
				self.led4.on()
			else:
				self.led4.off()

			if(distance < 60):
				self.led3.on()
			else:
				self.led3.off()

			if(distance < 40):
				self.led2.on()
			else:
				self.led2.off()

			if(distance < 20):
				self.led1.on()
			else:
				self.led1.off()

			print(distance, 'cm')
			time.sleep(0.03)

		self.clean_up()


	def clean_up(self):
		self.sens.cancel()
		self.led1.on()
		self.led2.off()
		self.led3.off()
		self.led4.off()


class SignalHandler:
	def __init__(self):
		self._running = True
		signal.signal(signal.SIGINT, self.turn_down)
		signal.signal(signal.SIGTERM, self.turn_down)


	def turn_down(self, signum, frame):
		self._running = False


	def can_run(self):
		return self._running



if __name__ == "__main__":

	gpa = GarageParkingAssistant(
		pi = '192.168.1.106',
		trig = 14,
		echo = 15,
		led1 = 18,
		led2 = 23,
		led3 = 24,
		led4 = 25,
		buzz = 8
	)

	gpa.start()

