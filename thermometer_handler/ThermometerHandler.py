class ThermometerHandler(object):
	
	def __init__(self, sensor_id):
		self.sensor_id = sensor_id


	def get_temperature(self):
		current_temperature = ''
		file = open('/sys/bus/w1/devices/' + self.sensor_id + '/' + 'w1_slave', 'r')
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

		

	def get_temperature_celsius(self):
		
		temp = self.get_temperature()
		
		if temp != 99999:
			print("Temperature in celsius: " + '{:.3f}'.format(int(temp)/float(1000)))
			
		return int(temp)/float(1000)
		

	def get_temperature_kelvin(self):
		
		temp = self.get_temperature()
		
		if temp != 99999:
			print("Temperature in kelvin: " + '{:.3f}'.format(int(temp)/float(1000) + 273.15))
	
		return int(temp)/float(1000) + 273.15
		
		
if __name__ == '__main__':

  tempSensor = ThermometerHandler('00-800000000000')
  tempSensor.get_temperature_celsius()
  tempSensor.get_temperature_kelvin()