from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class RoleAccessUser(AbstractUser):
    first_name = models.CharField(max_length=101)
    last_name = models.CharField(max_length=101)
    email = models.EmailField()
    is_Admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
