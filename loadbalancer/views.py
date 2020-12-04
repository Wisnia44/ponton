from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect

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

class UserSignupView (CreateView):
	template_name = 'registration/signup.html'
	form_class = UserCreationForm
	#success_url = reverse('index')
	def get_success_url(self):
		return reverse_lazy('home')

	def post (self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				)
			login(request, new_user)
			return HttpResponseRedirect("/home/")
		else:
			return HttpResponseRedirect("/signup2/")

class UserSignupView2 (CreateView):
	template_name = 'registration/signup2.html'
	form_class = UserCreationForm
	#success_url = reverse('index')
	def get_success_url(self):
		return reverse_lazy('home')

	def post (self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				)
			login(request, new_user)
			return HttpResponseRedirect("/home/")
		else:
			return HttpResponseRedirect("/signup2/")

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

class UserUnloggedView(View):
	template_name = 'loadbalancer/unlogged.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

#Main views
class HomeView (View):
	template_name = 'loadbalancer/home.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

class HelpView (View):
	template_name = 'loadbalancer/help.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})
