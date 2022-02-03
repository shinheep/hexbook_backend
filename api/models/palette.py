from django.db import models

class Palette(models.Model):
    hex1 = models.CharField(max_length=100)
    hex2 = models.CharField(max_length=100)
    hex3 = models.CharField(max_length=100)
    hex4 = models.CharField(max_length=100)

    def __str__(self):
        return self.hex1