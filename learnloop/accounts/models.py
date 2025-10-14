from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('mentor', 'Mentor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    
    phone_number = models.CharField(
        max_length=10, 
        blank=False, 
        null=True, 
        unique=True, 
    )
    
    def __str__(self):
        return self.username
