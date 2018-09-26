from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
#    first_name = models.CharField(max_length=50)
#    last_name = models.CharField(max_length=50)
#    username = models.CharField(max_length=50)
#    password = models.CharField(max_length=255)
#    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='restaurant_logo/', blank=False)
    
    
    def __str__(self):
        return self.name
