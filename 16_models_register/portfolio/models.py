from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class profile(models.Model):
    bio = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    birthdate = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.location)