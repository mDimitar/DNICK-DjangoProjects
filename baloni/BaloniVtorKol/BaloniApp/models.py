from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pilot(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    totalFlightHours = models.IntegerField()
    rank = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.surname

class Ballon(models.Model):
    type = models.CharField(max_length=50)
    manufacturerName = models.CharField(max_length=50)
    maxNumberOfPassenger = models.IntegerField()

    def __str__(self):
        return self.type

class AeroCompany(models.Model):
    name = models.CharField(max_length=50)
    yearOfCreation = models.IntegerField()
    fliesOutOfEurope = models.BooleanField()

    def __str__(self):
        return self.name

class Fligth(models.Model):
    code = models.CharField(max_length=10)
    airportNameDepart = models.CharField(max_length=50)
    airportNameArrive = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='testimages/')
    balloon = models.ForeignKey(Ballon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot,on_delete=models.CASCADE)
    aeroCompany = models.ForeignKey(AeroCompany,on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " " + self.balloon.type + " " + self.pilot.name + " " + self.aeroCompany.name

class PilotsInAeroCompany(models.Model):
    pilot = models.ForeignKey(Pilot,on_delete=models.CASCADE)
    aerocompany = models.ForeignKey(AeroCompany,on_delete=models.CASCADE)

    def __str__(self):
        return self.pilot.name + " " + self.aerocompany.name


