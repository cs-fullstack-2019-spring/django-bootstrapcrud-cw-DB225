from django.db import models

# Create your models here.
class GarageModel(models.Model):
    picture_URL  = models.CharField(max_length=800, default="")
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name