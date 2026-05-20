from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    ROLE_CHOICES = (
        ("attendee","Attendee"),
        ("organizer","Organizer"),
    )
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,default="attendee",choices=ROLE_CHOICES)
    
    def __str__(self):
        return self.username

