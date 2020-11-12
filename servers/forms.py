from django import forms
from .models import Service, Server

class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name',
        	'algorithm',
        	]

class ServerModelForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['address',
        	'analysis_method',
        	]
