class ThermometerHandler(object):

    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def get_temperature(self):
        
      try:
        current_temperature = ''
        file_name = 'w1_slave'
        file = open('/sys/bus/w1/devices/' + self.sensor_id + '/' + file_name, 'r')
        line = file.readline()
        check = line.rsplit(' ',1)
        check = check[1].replace('\n', '')
        
        if check == 'YES':
          line = file.readline()
          current_temperature = line.rsplit('t=',1)
        else:
          current_temperature = 99999
        file.close()
        
        return current_temperature[1]

      except:
        print('Error while getting temperature from sensor: ', self.sensor_id)
        return 99999

    def get_temperature_celsius(self):
        
        temp = self.get_temperature()
        
        if temp != 99999:
            print("Temp in celsius: " + '{:.3f}'.format(int(temp)/float(1000)))
            
        return int(temp)/float(1000)

    def get_temperature_kelvin(self):
        
        temp = self.get_temperature()
        
        if temp != 99999:
            print("Temp in kelvin: " + '{:.3f}'.format(int(temp)/float(1000) + 273.15))
    
        return int(temp)/float(1000) + 273.15
        
        
if __name__ == '__main__':

  tempSensor = ThermometerHandler('00-800000000000')
  tempSensor.get_temperature_celsius()
  tempSensor.get_temperature_kelvin()
