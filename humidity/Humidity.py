import RPi.GPIO as GPIO
import time
import mcp3204

class Humidity:
	
    def __init__(self):
		channel = 21;
        GPIO.setmode(GPIO.BOARD)
		GPIO.setup(channel, GPIO.IN)
        

    def run(self):
        try:
            while True:
				m = mcp3204.readadc(5)
				print "Moisture level: {:>5} ".format(m)
				sleep(.5)


if __name__ == "__main__":
    humidity = Humidity()
    humidity.run()