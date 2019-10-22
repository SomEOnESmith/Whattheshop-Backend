from django.contrib import admin
from .models import Profile, Crypto, Transaction, TransactionItem


# Customize admin page to track transations for different currencies

admin.site.register(Profile)

admin.site.register(Crypto)

admin.site.register(Transaction)

admin.site.register(TransactionItem)
