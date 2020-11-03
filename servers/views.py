from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.views.generic import (
	CreateView,
	DeleteView,
	DetailView,
	ListView,
	UpdateView,
	)
from .models import Service, Server
from .forms import ServiceModelForm, ServerModelForm

# Service based views
class ServiceCreateView(CreateView):
	template_name = 'servers/service-create.html'
	form_class = ServiceModelForm
	queryset = Service.objects.all()

	def get (self, request, *args, **kwargs):
		form = ServiceModelForm()
		return render(request, self.template_name, {'form': form})

	def get_success_url(self):
		return reverse('home')

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(ServiceCreateView, self).form_valid(form)


class ServiceDetailView(DetailView):
	template_name = 'servers/service.html'

	def get_queryset(self):
		return Service.objects.all()

class ServiceUpdateView(UpdateView):
	template_name = 'servers/service-update.html'
	queryset = Service.objects.all()

	def get (self, request, *args, **kwargs):
		form = ServiceModelForm()
		return render(request, self.template_name, {'form': form})

	def get_success_url(self):
		return reverse('home')

class ServiceDeleteView(DeleteView):
	template_name = 'servers/service-delete.html'
	queryset = Service.objects.all()

	def get (self, request, *args, **kwargs):
		form = ServiceModelForm()
		return render(request, self.template_name, {'form': form})

	def get_success_url(self):
		return reverse('home')

class ServiceListView(ListView):
	template_name = 'servers/service-list.html'

	def get_queryset(self):
		return Service.objects.filter(owner=self.request.user).values()

	def get_context_data(self, **kwargs):
		context = super(ServiceListView, self).get_context_data(**kwargs)
		service = Service.objects.filter(owner=self.request.user)
		context['service'] = service
		return context

#Server based views
class ServerCreateView(CreateView):
	template_name = 'servers/server-create.html'
	form_class = ServerModelForm
	queryset = Server.objects.all()

	def get (self, request, *args, **kwargs):
		form = ServerModelForm()
		return render(request, self.template_name, {'form': form})

	def get_success_url(self):
		return reverse('home')

	def form_valid(self, form):
		form.instance.service = Service.objects.get(pk=self.kwargs['pk'])
		return super(ServerCreateView, self).form_valid(form)

class ServerDetailView(DetailView):
	template_name = 'servers/server.html'

	def get_queryset(self):
		return Server.objects.all()

	def get_object(self):
		return Server.objects.get(pk=self.kwargs['pk2'])

class ServerUpdateView(UpdateView):
	template_name = 'servers/server-update.html'
	form_class = ServerModelForm
	queryset = Server.objects.all()

	def get (self, request, *args, **kwargs):
		form = ServerModelForm()
		return render(request, self.template_name, {'form': form})

	def get_success_url(self):
		return reverse('home')

	def get_object(self):
		return Server.objects.get(pk=self.kwargs['pk2'])

class ServerDeleteView(DeleteView):
	template_name = 'servers/server-delete.html'
	queryset = Server.objects.all()

	def get (self, request, *args, **kwargs):
		form = ServerModelForm()
		return render(request, self.template_name, {'form': form})

	def get_success_url(self):
		return reverse('home')

	def get_object(self):
		return Server.objects.get(pk=self.kwargs['pk2'])

class ServerListView(ListView):
	template_name = 'servers/server-list.html'

	def get_queryset(self):
		return Server.objects.filter(service=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(ServerListView, self).get_context_data(**kwargs)
		server = Server.objects.filter(service=self.kwargs['pk'])
		context['server'] = server
		return context
