from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    STATUS = [
        ('normal','Normal'),
        ('premium', 'Premium'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media/profile_pic', blank=True)
    description = models.CharField(null=True,max_length=100)

    
