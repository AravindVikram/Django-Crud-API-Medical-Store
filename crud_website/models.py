from django.db import models

# Create your models here.

class Medicine(models.Model):
   name = models.CharField(db_column='name', max_length=100, blank=False,null=True) 
   expiry_date=models.DateField(null=True)
   
   def __str__(self):
      return self.name



