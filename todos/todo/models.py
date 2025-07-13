from django.db import models
class shirts(models.Model):
    title = models.CharField(max_length=100)    
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class pants(models.Model):
    title = models.CharField(max_length=100)    
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class jackets(models.Model):
    title = models.CharField(max_length=100)    
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
            
# Create your models here.
