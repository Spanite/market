from django.contrib import admin
from .models import Client, Wallet, DepositWallet, Testimonials
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = 'Admin Panel'

admin.site.register(Client)
admin.site.register(Wallet)
admin.site.register(DepositWallet)
admin.site.register(Testimonials)

