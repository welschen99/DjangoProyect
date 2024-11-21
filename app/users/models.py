# """Users models."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    date_modified = models.DateTimeField(auto_now=True)
    sector = models.CharField(max_length=100)


    def __str__(self):
        """Return username."""
        return self.user.username

    @classmethod
    def get_active_users(cls):#El uso de cls en el método get_active_users se debe a que se trata de un método de clase (class method)
        return cls.objects.filter(is_active=True)