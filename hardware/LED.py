import pigpio

class LED:
	
	def __init__(self, pi, pin):
		self._pi = pi
		self._pin = pin
		
		self._pi.set_mode(self._pin, pigpio.OUTPUT)
	
	
	def on(self):
		self._pi.write(self._pin, 1)
		
		
	def off(self):
		self._pi.write(self._pin, 0)

