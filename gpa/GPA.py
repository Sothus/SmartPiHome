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
		
		self.distance_4 = 80
		self.distance_3 = 60
		self.distance_2 = 40
		self.distance_1 = 20
		
		self.sound_4 = 8000
		self.sound_3 = 1600
		self.sound_2 = 2000
		self.sound_1 = 4000
		
		self.buzz_on = 200
		self.buzz_off = 0
		
		self.pi.set_PWM_dutycycle(buzz, self.buzz_on)

		self.cleaner = SignalHandler()


	def start(self):
		self._running = True
		self._stopped = False
		while(self.cleaner.can_run() == True):

			distance = self.sens.read()

			if(distance < self.distance_4):
				self.led1.on()
				self.pi.set_PWM_dutycycle(self.buzz, self.buzz_on)
				self.pi.set_PWM_frequency(self.buzz, self.sound_4)
			else:
				self.led1.off()
				self.pi.set_PWM_dutycycle(self.buzz, self.buzz_off)


			if(distance < self.distance_3):
				self.led2.on()
				self.pi.set_PWM_dutycycle(self.buzz, self.buzz_on)
				self.pi.set_PWM_frequency(self.buzz, self.sound_3)
			else:
				self.led2.off()
				self.pi.set_PWM_dutycycle(self.buzz, self.buzz_off)

			if(distance < self.distance_2):
				self.led3.on()
				self.pi.set_PWM_dutycycle(self.buzz, self.buzz_on)
				self.pi.set_PWM_frequency(self.buzz, self.sound_2)
			else:
				self.led3.off()
				self.pi.set_PWM_dutycycle(self.buzz, self.buzz_off)

			if(distance < self.distance_1):
				self.led4.on()
				self.pi.set_PWM_dutycycle(self.buzz, self.buzz_on)
				self.pi.set_PWM_frequency(self.buzz, self.sound_1)
			else:
				self.led4.off()
				self.pi.set_PWM_dutycycle(self.buzz, self.buzz_off)

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

