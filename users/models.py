from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     pass


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
