from django.urls import path
from .views import (
    IndexView,
    ProfileView, 
    Cfds,
    Crypto,
    indecies,
    Forex,
    Stock,Commodities,Tc,Ta,Tips,Lm,Fa,Wait,
    )

app_name = "main"

urlpatterns = [
    path('', IndexView, name="index"),
    path('profileview', ProfileView, name="profile"),
    path('cfds', Cfds, name="cfds"),
    path('crypto', Crypto, name="crypto"),
    path('forex', Forex, name="forex"),
    path('indecies',indecies, name="indecies"),
    path('stock', Stock , name="stock"),
    path('commodities', Commodities, name="commodities"),

    path('lm/', Lm, name="lm"),
    path('fa/', Fa, name= "fa"),
    path('tips/', Tips, name="tips"),
    path('ta/', Ta, name="ta"),
    path('tc/', Tc, name="tc"),
    path('wait/', Wait, name="wait"),
    
]
