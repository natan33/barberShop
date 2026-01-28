from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    is_client = models.BooleanField(default=True)
    is_barber = models.BooleanField(default=True)

    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
     

class Barber(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='barber_profile'
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username