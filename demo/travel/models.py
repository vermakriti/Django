from django.db import models

# Create your models here.
class Destination(models.Model):
   
    name= models.CharField(max_length=10)
    image= models.ImageField(upload_to='pics')
    price= models.IntegerField(null=True)
    offer= models.BooleanField(default=False)


    def __str__(self):
        return self.name