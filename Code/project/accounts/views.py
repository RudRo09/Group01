from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# verification imports
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			phone_number = form.cleaned_data['phone_number']
			password = form.cleaned_data['password']
			username = email.split('@')[0]  	# creating username from email address

			# create user object
			user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,\
				username=username, password=password)
			user.phone_number = phone_number
			user.save()

			# user activation
			current_site = get_current_site(request)
			mail_subject = 'Account Activation Link'
			message = render_to_string('accounts/verfication_email.html', {
				'user': user,
				'domain': current_site,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),			# encoding primary key
				'token': default_token_generator.make_token(user),
				})
			email_to = email
			send_email = EmailMessage(mail_subject, message, to=[email_to])
			send.email.send()

			messages.success(request, 'Registration Successful!')
			return redirect('register')

	else:
		form = RegistrationForm()

	context = {
		'form': form,
	}
	return render(request, 'accounts/register.html', context)


def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		user = auth.authenticate(email=email, password=password)

		if user is not None:
			auth.login(request, user)
			# messages.success(request, 'Log in Successful!')
			return redirect('home')

		else:
			messages.error(request, 'The email and password you entered did not match our records. Please double-check and try again!')
			return redirect('login')

	return render(request, 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
	auth.logout(request)
	messages.success(request, 'Logged Out!')
	return redirect('login')


def activate(request):
	pass
