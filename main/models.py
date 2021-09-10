from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
PLANS =(
		('basic', 'basic'),
		('gold', 'gold'),
		('platnum', 'platnum'),
		('vip', 'vip'),

)

CURRENCY =(
	( 'USD', 'USD'),
	( 'EUR', 'EUR'),
	( 'GBP','GBP'),

)


class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=100)
	image = models.ImageField(blank=True, null=True, upload_to="media", default="img/no-image.png")
	userid = models.CharField(blank=True, max_length=10)
	bill = models.PositiveIntegerField(blank=True, null=True)
	plan = models.CharField(max_length=8, choices=PLANS, blank=True, null=True)
	active = models.CharField(max_length=10, blank=True)
	earning_session = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return f'{self.user} {self.userid} {self.bill} '

	def get_client(self):
		return self.Client.all()


	def save(self, *args, **kwargs):
		if self.userid == "":
			self.userid = str(uuid.uuid4()).replace("-", "").lower()[:8]

		return super().save(*args, **kwargs)

class Wallet(models.Model):
	email = models.EmailField()
	wallet_address = models.CharField(max_length=100)
	currency = models.CharField(max_length=3, choices=CURRENCY)
	amount = models.FloatField()

	def __str__(self):
		return self.wallet_address
	
class DepositWallet(models.Model):
	image = models.ImageField(blank=True, null=True, upload_to="media")
	main_wallet= models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.main_wallet
	

class Testimonials(models.Model):
	name = models.CharField(max_length=100)
	textfield = models.TextField()
	image = models.ImageField(upload_to='media', blank=True, null=True)
	title = models.CharField(max_length=100)

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	def __str__(self):
		return str(self.name)



def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
