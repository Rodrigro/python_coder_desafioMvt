from django.db import models

# Create your models here.

class Familiares(models.Model):
    name=models.CharField(max_length=50)
    identification=models.IntegerField()
    is_parent= models.BooleanField()
   
    
