from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=19, decimal_places=10)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="wallet")

class Crypto(models.Model):
	currency = models.CharField(max_length=150)
	price = models.DecimalField(max_digits= 10, decimal_places=3)
	image = models.ImageField(null=True, blank=True)
	rate_change = models.DecimalField(max_digits=6, decimal_places=3)