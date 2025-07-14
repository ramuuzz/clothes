from django.db import models
class shirts(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,default=1,related_name='shirts')
    title = models.CharField(max_length=100)    
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class pants(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,default=1 ,related_name='pants')
    title = models.CharField(max_length=100)    
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class jackets(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,default=1, related_name='jackets')
    title = models.CharField(max_length=100)    
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
            
# Create your models here.
