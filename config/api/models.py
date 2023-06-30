from django.db import models


# Create your models here.
class Car(models.Model):
    ENGINE_CHOICES = [
        ("diesel", "Diesel"),
        ("essence", "Essence"),
        ("electrique", "Électrique"),
    ]
    brand = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.TextField()
    engine = models.CharField(max_length=50, choices=ENGINE_CHOICES)
    year = models.IntegerField()
    description = models.TextField()
    km = models.IntegerField()


class Contact(models.Model):
    title = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
