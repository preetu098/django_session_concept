from django.db import models

# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.username