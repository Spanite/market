from django.shortcuts import render
from .models import Client
from sfinancialmarket.forms import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def IndexView(request):
    post = Client.objects.get(user=request.user)
    context = {
        "post":post
    }
    return render(request, 'main/index.html', context)

@login_required
def ProfileView(request):
    profile = Profile(request.POST or None)
    if request.method == 'POST':
        date_of_birth = request.POST.get('date_of_birth')
        phonenumber = request.POST.get('phonenumber')
        country = request.POST.get('country')
        account = request.POST.get('account')

    context={
        'profile':profile
    }
    return render(request, 'main/profile.html', context)

def reviews(request):
    test = Testimonials.objects.all()
    context = {'test':test}
    return render(request, 'landing_page.html', context)

def Wait(request):
    return render(request, "main/wait.html")

def Cfds(request):
    return render(request, "main/cfds.html")


def Crypto(request):
    return render(request, "main/crypto.html")


def indecies(request):
    return render(request, "main/indecies.html")

def Forex(request):
    return render(request, "main/fx.html")

def Stock(request):
    return render(request, "main/stock.html")

def Commodities(request):
    return render(request, "main/commodities.html")


def Tc(request):
    return render(request, "main/tc.html")


def Ta(request):
    return render(request, "main/ta.html")


def Tips(request):
    return render(request, "main/tips.html")


def Lm(request):
    return render(request, "main/lm.html")

def Fa(request):
    return render(request, "main/fa.html")