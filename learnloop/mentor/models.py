from django.db import models

# Create your models here.
# mentor/models.py
from django.db import models
from accounts.models import CustomUser

class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments')
    mentor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mentor_appointments')
    date = models.DateField(
        auto_now=True,
    )
    time = models.TimeField(
        auto_created=True   
    )
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.mentor} on {self.date}"
