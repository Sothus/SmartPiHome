import RPi.GPIO as GPIO
import time
import pigpio

class RGBControl:
	
	#~ #def __init__(self, host, port, pinR, pinG, pinB):
	
    def __init__(self, host,  port, pinR, pinG, pinB):
        self.colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]
        self.pins = {'pinR':pinR, 'pinG':pinG, 'pinB':pinB}
        self.pi = pigpio.pi(host, port)
        if not self.pi.connected:
			exit()
        
        #~ PIO.setmode(GPIO.BOARD)
        #~ for i in self.pins:
            #~ GPIO.setup(self.pins[i], GPIO.OUT)
            #~ GPIO.output(self.pins[i], GPIO.HIGH)
        
        for i in self.pins:
			self.pi.set_mode(self.pins[i], pigpio.OUTPUT)
			self.pi.write(self.pins[i], 1)
          

        #~ self.pR = GPIO.PWM(self.pins['pinR'], 2000)
        #~ self.pG = GPIO.PWM(self.pins['pinG'], 3000)
        #~ self.pB = GPIO.PWM(self.pins['pinB'], 5000)
        

        self.pi.set_PWM_dutycycle(self.pins['pinR'],50) # Start/stop PWM pulses on a GPIO
        self.pi.set_PWM_dutycycle(self.pins['pinG'],50)
        self.pi.set_PWM_dutycycle(self.pins['pinB'],50)

        #~ self.pR.start(0)
        #~ self.pG.start(0)
        #~ self.pB.start(0)
        #~ self.pR.set_PWM_dutycycle()
        #~ pi.set_PWM_dutycle(self.pins['pinR'], 255)

    def setColor(self, col):
        Rval = (col & 0xFF0000) >> 16
        Gval = (col & 0x00FF00) >> 8
        Bval = (col & 0x0000FF) >> 0
        
        #mapping
        Rval = (Rval - 0) * (100 - 0) / (255 - 0) + 0
        Gval = (Gval - 0) * (100 - 0) / (255 - 0) + 0
        Bval = (Bval - 0) * (100 - 0) / (255 - 0) + 0
        
        #~ self.pR.ChangeDutyCycle(Rval)
        #~ self.pG.ChangeDutyCycle(Gval)
        #~ self.pB.ChangeDutyCycle(Bval)
        
        self.pi.set_PWM_frequency(self.pins['pinR'], Rval)
        self.pi.set_PWM_frequency(self.pins['pinG'], Gval)
        self.pi.set_PWM_frequency(self.pins['pinB'], Bval)


    def run(self):
        try:
            while True:
                for col in self.colors:
                    self.setColor(col)
                    time.sleep(0.5)
        except KeyboardInterrupt:
            #~ self.pR.stop()
            #~ self.pG.stop()
            #~ self.pB.stop()
            for i in self.pins:
                #~ GPIO.output(self.pins[i], GPIO.HIGH)
				self.pi.write(self.pins[i], 1)
            #GPIO.cleanup()

if __name__ == "__main__":
    rgbControl = RGBControl('raspberrypi', 8888, 11,12,13)
    rgbControl.run()
