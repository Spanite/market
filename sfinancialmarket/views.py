from django.views import generic
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Profile, CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from main.models import Testimonials



class LandingPage(generic.TemplateView):
	template_name = "landing_page.html"


def login_view(request):
	error_message = None
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				if request.GET.get('next'):
					return redirect(request.GET.get('next'))
				else:
					return redirect('main:index')
		else:
			error_message = 'oops... something went wrong'
	context = {
		'form': form,
		'error_message': error_message
	}

	return render(request, 'auth/login.html', context)


def logout_view(request):
	logout(request)
	return redirect('login')


class ProfileView (generic.CreateView):
	template_name = "main/profile.html"
	form_class = Profile

	def get_success_url(self):
		return reverse("login")

def Signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'CONFIRMATION '
			message = render_to_string('mail.html',{
				'user': user
			})
			plain_message = strip_tags(message)
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
						mail_subject, plain_message, to=[to_email]
			)
			email.send()
			return redirect('main:profile')
			
	else:
		form = CustomUserCreationForm()
	return render(request, 'auth/signup.html', {'form': form})


def Reviews(request):
	reviews = Testimonials.objects.all()
	context ={
		'reviews':reviews
	}

	return render(request, "landing_page.html", context)	