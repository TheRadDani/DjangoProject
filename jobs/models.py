from django.db import models

# Create your models here.
class Jobs(models.Model):
    #images
    image = models.ImageField(upload_to='images/') #pip3 install pillow
    #sumary
    sumary = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.sumary