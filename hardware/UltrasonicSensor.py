import time
import pigpio


class UltrasonicSensor:
	
	
	def __init__(self, pi, trigger, echo):
		self.pi = pi
		self._trig = trigger
		self._echo = echo
		
		self._ping = False
		self._high = None
		self._time = None
		
		self._triggered = False
		
		self._trig_mode = pi.get_mode(self._trig)
		self._echo_mode = pi.get_mode(self._echo)
		
		pi.set_mode(self._trig, pigpio.OUTPUT)
		pi.set_mode(self._echo, pigpio.INPUT)
		
		self._cb = pi.callback(self._trig, pigpio.EITHER_EDGE, self._cbf)
		self._cb = pi.callback(self._echo, pigpio.EITHER_EDGE, self._cbf)
		
		self._inited = True
		
	
	def _cbf(self, gpio, level, tick):
		if((gpio == self._trig) and (level == 0)): # trigger sent
			self._triggered = True
			self._high = None
		elif(self._triggered):
			if(level == 1):
				self._high = tick
			elif self._high is not None:
				self._time = tick - self._high
				self._high = None
				self._ping = True
				
						
	def read(self):
		if self._inited:
			self._ping = False
			self.pi.gpio_trigger(self._trig)
			start = time.time()
			while not self._ping:
				if (time.time()-start) > 1.0:
					return 20000
				time.sleep(0.001)
			return round((self._time / 1000000.0 * 34030), 2)
		else:
			return None
			
			
	def cancel(self):
		if self._inited:
			self._inited = False
			self._cb.cancel()
			self.pi.set_mode(self._trig, self._trig_mode)
			self.pi.set_mode(self._echo, self._echo_mode)
			

