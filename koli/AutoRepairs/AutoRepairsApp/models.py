from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    creationDate = models.IntegerField()
    fixesOldtimer = models.BooleanField()

    def __str__(self):
        return self.name + " " + str(self.creationDate) + " " + str(self.fixesOldtimer)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    countryOrigin = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    type = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    maxSpeed = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.type + " " + str(self.maxSpeed)

class Repair(models.Model):
    code = models.CharField(max_length=20)
    date = models.DateField()
    description = models.TextField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop,on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " " + str(self.date) + " " + self.description + " " + self.workshop.name

class ManufacturerWorkshop(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop,on_delete=models.CASCADE)

    def __str__(self):
        return self.manufacturer.name + " " + self.workshop.name