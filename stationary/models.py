from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TransactionItem(models.Model):
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.quantity} {self.product} - ${self.total()}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return f'{self.user.username} Profile'


