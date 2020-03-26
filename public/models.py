from django.db import models

# Create your models here.
class PublicData(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    voted = models.BooleanField(default=False)
    pic = models.ImageField(upload_to ='uploads/')
    ready = models.BooleanField(default=False)
    
    def __str__(self):
        return self.firstname