from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
