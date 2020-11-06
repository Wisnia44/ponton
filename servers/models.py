from django.db import models
from django.conf import settings
from django.db import models


# Create your models here.
class Service(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	algorithms_choices =[
		('round_robin','round_robin'),
		('lowest_ping_time', 'lowest_ping_time'),
		('lowest_cpu_usage', 'lowest_cpu_usage'),
		]
	algorithm = models.CharField(
		max_length=20, 
		choices=algorithms_choices, 
		default='round_robin'
		)
	name = models.CharField(max_length=15)
	request_counter = models.IntegerField(default=0)

	def get_absolute_url(self):
		return reverse("service", kwargs={"pk": self.pk})

	def get_owner(self):
		return self.owner

class Server(models.Model):
	address = models.CharField(max_length=15)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	cpu_state = models.FloatField(default=0.5)
	ping_interval = models.IntegerField(default=300)
	last_time_checked = models.DateTimeField(default=None, null=True)
	status_choices =[
		('ready','ready'),
		('not_responding', 'not_responding'),
		('no_cpu_state', 'no_cpu_state'),
		]
	status = models.CharField(
		max_length=20, 
		choices=status_choices, 
		default='ready'
		)

	def get_owner(self):
		#obj = Service.objects.get(pk=self.service)
		return service.owner
