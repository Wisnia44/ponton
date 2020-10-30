from django.db import models

# Create your models here.
class Service():
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	algorithms_choices =[
		('round_robin','round_robin'),
		]
	algorithm = models.CharField(
		max_length=15, 
		choices=bayess_filter_choices, 
		default='round_robin'
		)

	def get_absolute_url(self):
		return reverse("service", kwargs={"pk": self.pk})

	def get_owner(self):
		return self.owner

class Server():
	address = models.CharField(max_length=15)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)

	def get_owner(self):
		obj = Service.objects.get(pk=self.service)
		return obj.owner
