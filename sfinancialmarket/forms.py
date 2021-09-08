from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from main.models import Client, Wallet

ACCOUNT_TYPE =(
    ( 'Basic', 'basic(Forex, Commodities)'),
    ( 'Gold','gold(Forex, Stocks, Commodities, Crypto)'),
    ( 'Platnum','platnum(Forex, Stocks, Commodities, Crypto, indicies )'),
    ( 'VIP','vip(Forex, Stocks, Commodities, Crypto, indicies )')

)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (           
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
                 
        )
        field_classes = {'username': UsernameField}

    


class Profile(forms.Form):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    phonenumber = PhoneNumberField().formfield()
    account = forms.ChoiceField(choices=ACCOUNT_TYPE)
    country = CountryField(blank_label='(Select Country)').formfield()
    I_agree_to_terms_and_conditions = forms.BooleanField()


    class Meta:
        model = Client
        fields = (
        
            'date_of_birth',    
            'phone_number',
            'account',
            'country',
        )


class WalletForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = (

                'email',
                'wallet_address',
                'currency',
                'amount',
        
            )                                                                                                                                                                                                                              
                                                                                               