from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    phone_number = models.CharField(max_length=8, null=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username
    

class Crypto(models.Model):
    currency = models.CharField(max_length=150)
    price = models.DecimalField(max_digits= 10, decimal_places=3)
    image = models.ImageField(null=True, blank=True)
    rate_change = models.DecimalField(max_digits=6, decimal_places=3)


class Transaction(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=6, decimal_places=3)
    # Add related name
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class TransactionItem(models.Model):
    # Adjust related names
    currency = models.ForeignKey(Crypto, on_delete=models.CASCADE, related_name="transactionitem")
    transation = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="transactionitem")
    quantity = models.PositiveIntegerField()
    



    
