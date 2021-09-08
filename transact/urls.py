from django.urls import path
from .views import Deposit, Withdraw, Account

app_name = 'transact'

urlpatterns = [
    path("deposit", Deposit, name="deposit"),
    path("withdraw/", Withdraw, name="withdraw"),
    path('account', Account, name="account"),
]
