from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True,auto_created=True)
    city = models.CharField(max_length=100,default="unknown")

    def __str__(self):
        return self.name