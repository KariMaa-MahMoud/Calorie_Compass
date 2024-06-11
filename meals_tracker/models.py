from django.db import models


# Create your models here.
class food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    protiens = models.DecimalField(max_digits=4, decimal_places=1)
    fats = models.DecimalField(max_digits=4, decimal_places=1)

