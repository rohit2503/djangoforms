from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "Person"

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=25)

    class Meta:
        db_table = "Car"

    def __str__(self):
        return self.make


class AssignCar(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="person")
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name="Car")

    class Meta:
        db_table = "AssignCar"