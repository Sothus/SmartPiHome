from django.db import models

class RaspberryPi(models.Model):
	name = models.CharField(max_length=200,
							db_index=True)
	address = models.CharField( max_length=20,
								db_index=True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name
		

class Light(models.Model):
	name = models.CharField(max_length=200,
							db_index=True)
	pin = models.IntegerField()
	is_on = models.BooleanField(default=False)
	
	pi = models.ForeignKey(
		"RaspberryPi",
		on_delete=models.CASCADE,
		default=0,
	)
	
	def __str__(self):
		return self.name


class RGBLight(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200,
							db_index=True)
	pinRed = models.IntegerField()
	pinGreen = models.IntegerField()
	pinBlue = models.IntegerField()
	
	is_on = models.BooleanField(default=False)
	
	colorRed 	= models.IntegerField()
	colorGreen	= models.IntegerField()
	colorBlue 	= models.IntegerField()
	
	pi = models.ForeignKey(
		"RaspberryPi",
		on_delete=models.CASCADE,
		default=0,
	)
	
	def __str__(self):
		return self.name

		
class TemperatureSensor(models.Model):
	name = models.CharField(max_length=200,
							db_index=True)
	sensor_id = models.CharField(max_length=15,
								 db_index=True)
								 
	def __str__(self):
		return self.name
		
								 
class GPA(models.Model):
	name = models.CharField(max_length=200,
							db_index=True)
	pi = models.ForeignKey(
		"RaspberryPi",
		on_delete=models.CASCADE,
		default=0,
	)
	pinEcho = models.IntegerField()
	pinTrig = models.IntegerField()
	pinLed1 = models.IntegerField()
	pinLed2 = models.IntegerField()
	pinLed3 = models.IntegerField()
	pinLed4 = models.IntegerField()
	pinBuzz = models.IntegerField()
	
	def __str__(self):
		return self.name
		

class HumiditySensor(models.Model):
	name = models.CharField(max_length=200,
							db_index=True)
	
	channel = models.IntegerField()
	
	pi = models.ForeignKey(
		"RaspberryPi",
		on_delete=models.CASCADE,
		default=0,
	)
								 
	def __str__(self):
		return self.name
