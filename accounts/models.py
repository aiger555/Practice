from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import ModelState

class User(AbstractUser):
    class TypeUserChoice(models.TextChoices):
        ADMIN = 'admin'
        SPECIALIST = 'specialist'
        PERSONAL_CABINET = 'personal_cabinet'

    middle_name = models.CharField(max_length=128, blank=True)
    type_user = models.CharField(max_length=50, 
                                choices=TypeUserChoice.choices,
                                default=TypeUserChoice.PERSONAL_CABINET)

