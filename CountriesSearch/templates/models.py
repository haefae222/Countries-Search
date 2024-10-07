from django.db import models

# Create your models here.
class MyCountries(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = "Countries"
    
    def __str__(self):
        return self.name