from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.urls import reverse
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import (
	UserCreationForm, 
	AuthenticationForm, 
	UserChangeForm, 
	PasswordChangeForm
	)
from django.views.generic import (
	CreateView,
	DeleteView,
	DetailView,
	ListView,
	UpdateView,
	)
from .forms import UserUpdateForm

# User based views
class UserLoginView (View):
	template_name = 'loadbalancer/user_login.html'
	def post (self, request, *args, **kwargs):
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('home')
		else:
			return redirect('home')
	def get (self, request, *args, **kwargs):
		form = AuthenticationForm()
		return render(request, self.template_name, {'form': form})

class UserLogoutView (View):
	def post (self, request, *args, **kwargs):
		logout(request)
		return redirect('home')

class UserUpdateView (View):
	template_name = 'loadbalancer/user_update.html'
	model = User
	success_url = 'loadbalancer/user_update.html'
	def post (self, request, *args, **kwargs):
		form = UserUpdateForm(data=request.POST, instance=request.user)
		form.fields['first_name'].initial = request.user.first_name
		form.fields['last_name'].initial = request.user.last_name
		form.fields['email'].initial = request.user.email
		if form.is_valid():
			form.save()
		return redirect('home')
	def get(self, request, *args, **kwargs):
		form = UserUpdateForm()
		form.fields['first_name'].initial = request.user.first_name
		form.fields['last_name'].initial = request.user.last_name
		form.fields['email'].initial = request.user.email
		return render(request, self.template_name, {'form': form})	

class UserDeleteView (DeleteView):
	template_name = 'loadbalancer/user_delete.html'
	def get (self, request, *args, **kwargs):
		return render(request, self.template_name, {})
	def post(self, request, *args, **kwargs):
		user = User.objects.get(pk=request.user.pk)
		user.delete()
		return redirect('home') 

class UserSignupView (View):
	template_name = 'loadbalancer/user_signup.html'
	def post (self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
		else:
			raise ValidationError("Spróbuj jeszcze raz")

	def get (self, request, *args, **kwargs):
		form = UserCreationForm()
		return render(request, self.template_name, {'form': form})

class UserChangePassword(View):
	template_name = 'loadbalancer/user_change_password.html'
	def post (self, request, *args, **kwargs):
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('home')
	def get (self, request, *args, **kwargs):
		form = PasswordChangeForm(request.user)
		return render(request, self.template_name, {'form': form})


#Main views
class HomeView (View):
	template_name = 'loadbalancer/home.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})
