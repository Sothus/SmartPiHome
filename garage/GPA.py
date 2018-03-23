import pigpio, time
from UltrasonicSensor import UltrasonicSensor

if __name__ == "__main__":
	pi = pigpio.pi('192.168.1.106')
	sonar = UltrasonicSensor(pi, 14, 15)
	end = time.time() + 600.0
	r = 1
	while time.time() < end:
		distance = sonar.read()
		distance = round(distance, 2)
		print("{} {}".format(r, distance))
		r += 1
		time.sleep(0.03)
		
	sonar.cancel()
	pi.stop()
