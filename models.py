from __future__ import unicode_literals  
from django.db import models

# Create your models here.

class Customers(models.Model):

    first_Name=models.CharField(max_length=30)
    last_Name=models.CharField(max_length=30)

    class Meta:

        db_table='Customers'

