from django.shortcuts import render
from django.views import View
from django.views.generic import (
	CreateView,
	DeleteView,
	DetailView,
	ListView,
	UpdateView,
	)

# Service based views
class ServiceCreateView(CreateView):
	pass

class ServiceDetailView(View):
	pass

class ServiceUpdateView(View):
	pass

class ServiceDeleteView(DeleteView):
	pass

class ServiceListView(View):
	pass




#Server based views
class ServerCreateView(View):
	pass

class ServerDetailView(View):
	pass

class ServerUpdateView(View):
	pass

class ServerDeleteView(View):
	pass

class ServerListView(View):
	pass
