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

    def __str__(self):
        return self.name

class RGBLight(Light):
    pass

class DistanceSensor(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    trigger_pin = models.IntegerField()
    echo_pin = models.IntegerField()

    def __str__(self):
        return self.name
# Create your models here.
