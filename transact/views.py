from django.shortcuts import render, redirect, reverse
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.views import generic
from main.models import Client, DepositWallet, Wallet
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from sfinancialmarket.forms import WalletForm
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags


# Create your views here.
@login_required
def Withdraw(request):
	if request.method == 'POST':
		form = WalletForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			#current_site = get_current_site(request)
			mail_subject = 'WITHDRAWAL REQUEST'
			message = render_to_string('withmail.html')
			plain_message = strip_tags(message)
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
						mail_subject, plain_message, to=[to_email]
			)
			email.send()
			return redirect('main:index')
			
	else:
		form = WalletForm()
	return render(request, 'transact/withdraw.html', {'form': form})





@login_required
def Deposit(request):
	lead = DepositWallet.objects.all()
	context = {
		"lead": lead
	  }
	return render(request, 'transact/deposite.html', context)


def Account(request):
	return render(request, "transact/account.html")




	