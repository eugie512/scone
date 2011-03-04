from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    list_date = models.DateField('Date Listed')
    
    def __unicode__(self):
        return self.title