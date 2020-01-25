from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class Object(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField()
    original_price = models.IntegerField(default=0)
    lir_price = models.IntegerField(default=0)

