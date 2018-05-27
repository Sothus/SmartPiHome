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
		
		self.pi.set_PWM_dutycycle(buzz, 200)

		self.cleaner = SignalHandler()



	def start(self):
		self._running = True
		self._stopped = False
		while(self.cleaner.can_run() == True):

			distance = self.sens.read()

			if(distance < 80):
				self.led1.on()
				self.pi.set_PWM_dutycycle(self.buzz, 200)
				self.pi.set_PWM_frequency(self.buzz, 8000)
			else:
				self.led1.off()
				self.pi.set_PWM_dutycycle(self.buzz, 0)


			if(distance < 60):
				self.led2.on()
				self.pi.set_PWM_dutycycle(self.buzz, 200)
				self.pi.set_PWM_frequency(self.buzz, 1600)
			else:
				self.led2.off()
				self.pi.set_PWM_dutycycle(self.buzz, 0)

			if(distance < 40):
				self.led3.on()
				self.pi.set_PWM_dutycycle(self.buzz, 200)
				self.pi.set_PWM_frequency(self.buzz, 2000)
			else:
				self.led3.off()
				self.pi.set_PWM_dutycycle(self.buzz, 0)

			if(distance < 20):
				self.led4.on()
				self.pi.set_PWM_dutycycle(self.buzz, 200)
				self.pi.set_PWM_frequency(self.buzz, 4000)
			else:
				self.led4.off()
				self.pi.set_PWM_dutycycle(self.buzz, 0)

			#print(distance, 'cm')
			time.sleep(0.03)

		self.clean_up()


	def clean_up(self):
		self.sens.cancel()
		self.led1.on()
		self.led2.off()
		self.led3.off()
		self.led4.off()
		self.pi.set_PWM_dutycycle(self.buzz, 0)


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
		pi = '192.168.1.105',
		trig = 14,
		echo = 15,
		led1 = 18,
		led2 = 23,
		led3 = 24,
		led4 = 25,
		buzz = 8
	)

	gpa.start()

