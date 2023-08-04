from django.db import models

# Create your models here.
class SalesModel(models.Model):
    merchandiseID =  models.CharField(max_length=6)
    merchandise = models.CharField(max_length=10)
    unitPrice = models.IntegerField()

    def __str__(self) -> str:
        return self.merchandise