from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=200)
    Hero = models.CharField(max_length=200)
    Race = models.CharField(max_length=200)
    Strength = models.IntegerField()
    Constitution= models.IntegerField()
    Dexterity = models.IntegerField()
    Intelligence= models.IntegerField()
    Wisdom = models.IntegerField()
    Charisma = models.IntegerField()
    