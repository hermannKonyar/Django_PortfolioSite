from django.db import models

class About(models.Model):
    description = models.TextField()
    image = models.CharField(max_length=250)
    email = models.EmailField()
    adress = models.CharField(max_length=250)

class Skill(models.Model):
    title = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    

class Experience(models.Model):
    date=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    description=models.TextField()
    position = models.CharField(max_length=100)
