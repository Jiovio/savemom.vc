from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Mother(models.Model):
    mother_id = models.CharField(max_length=20, unique=True)
    mother_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  # Assuming a standard phone number length

    def __str__(self):
        return self.mother_name

class CustomUser(models.Model):
    username = models.CharField(max_length=255)  # Change 'name' to 'username'
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)