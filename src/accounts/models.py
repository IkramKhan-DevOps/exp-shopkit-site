from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    PRE: need to migrate accounts application at the start
    """
    is_client = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Users"
        ordering = ['-date_joined']

    def __str__(self):
        return self.username


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Clients Profiles"

    def __str__(self):
        return self.user.username
    