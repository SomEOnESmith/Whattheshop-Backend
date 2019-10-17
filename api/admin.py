from django.contrib import admin
from .models import Profile, Wallet, Crypto


# Customize admin page to track transations for different currencies

admin.site.register(Profile)
admin.site.register(Wallet)
admin.site.register(Crypto)
