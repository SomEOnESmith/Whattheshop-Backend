from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    phone_number = models.CharField(max_length=9,null=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username


class Wallet(models.Model):
    money = models.DecimalField(max_digits=19, decimal_places=10)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="wallet")
    

class Crypto(models.Model):
    currency = models.CharField(max_length=150)
    price = models.DecimalField(max_digits= 10, decimal_places=3)
    image = models.ImageField(null=True, blank=True)
    rate_change = models.DecimalField(max_digits=6, decimal_places=3)

class TransactionItem(models.Model):
    currency = models.ForeignKey(Crypto, on_delete=models.CASCADE, related_name="transactionitem")
    quantity = models.PositiveIntegerField()
    
    
class Transaction(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=6, decimal_places=3)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    Currency = models.ForeignKey(Crypto, on_delete=models.CASCADE, related_name="transaction")


    
