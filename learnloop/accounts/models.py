from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

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
    phone_regex = RegexValidator(
    regex=r'^[9876]\d{9}$',
    message="Phone number must be a 10-digit number and start with 9, 8, 7, or 6."
    )
    phone_number = models.CharField(
        max_length=10, 
        blank=True, 
        null=True, 
        validators=[phone_regex],
        unique=True,
        help_text='Enter 10 digit phone number'
        
    )

    previous_experience = models.BooleanField(blank=True, null=True)

    is_approved=models.BooleanField(default=False)
    
    def __str__(self):
        return self.username