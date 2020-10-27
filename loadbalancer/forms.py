from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        	'first_name', 
        	'last_name', 
        	'email', 
        	]
        exclude = (
        	'last_login',
        	'date_joined',
        	'is_superuser',
        	'is_active',
        	'is_staff',
        	'user_permissions',
        	'groups',
        	'password',
        	)
