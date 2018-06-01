import spidev
import time

class Humidity:
        def __init__(self, spi_channel=1):
                self.spi_channel = spi_channel
                self.conn = spidev.SpiDev(0, spi_channel)
                self.conn.max_speed_hz = 1000000 # 1MHz
                

        def __del__( self ):
                self.close
                

        def close(self):
                if self.conn != None:
                        self.conn.close
                        self.conn = None
                        

        def bitstring(self, n):
                s = bin(n)[2:]
                return '0'*(8-len(s)) + s
                

        def read(self, adc_channel=0):
                # build command
                cmd  = 128 # start bit
                cmd +=  64 # single end / diff
                if adc_channel % 2 == 1:
                        cmd += 8
                if (adc_channel/2) % 2 == 1:
                        cmd += 16
                if (adc_channel/4) % 2 == 1:
                        cmd += 32

 
                reply_bytes = self.conn.xfer2([cmd, 0, 0, 0])

                reply_bitstring = ''.join(self.bitstring(n) for n in reply_bytes)
                reply = reply_bitstring[5:19]
                return int(reply, 2)
                

if __name__ == '__main__':
        
        spi = MCP3208()
        
        analog0 = 0

        while True:       
                a0 = spi.read(0)
                print("ch0=%01d" % a0)
                time.sleep(1)
