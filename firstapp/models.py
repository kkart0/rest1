from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    rating=models.FloatField(max_length=10)
    image=models.ImageField(default="")

    def __str__(self):
        return self.name