from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('mentor', 'Mentor'),
        ('Admin', 'Admin'),
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user'
    )
    
    phone_number = models.CharField(
        max_length=10, 
        blank=True, 
        null=True, 
        unique=True,
        help_text='Enter 10 digit phone number'
    )

    previous_experience = models.BooleanField(blank=True, null=True)

    is_approved=models.BooleanField(default=False)
    
    def __str__(self):
        return self.username