from celery import shared_task
from .models import Server, Service
from .funcs import ping_time
from django.db.utils import IntegrityError

@shared_task
def count_servers():
	return Server.objects.count

@shared_task(name='ping_servers')
def ping_servers():
	sum_rtt_avg = 0
	services = Service.objects.filter(algorithm='lowest_ping_time')
	for service in services:
		servers = Server.objects.filter(service=service)
		for server in servers:
			if "https://" in server.address:
				address = server.address[8:]
			elif "http://" in server.address:
				address = server.address[7:]
			else:
				address = server.address
			if address[-1] == '/':
				address = address[:-1]
			rtt_avg = ping_time(address)
			if rtt_avg is not None:
				try:
					sum_rtt_avg += rtt_avg
					server.ping_time = rtt_avg
					server.save()
				except IntegrityError:
					print("Server with server.pk = {} cannot be saved".format(server.pk))
					server.ping_time = 9999.0
					server.save()
			else:
				print("Server with server.pk = {} cannot be reached".format(server.pk))
				server.ping_time = 9999.0
				server.save()
	print("Sum of rtt_avgs equals {}".format(sum_rtt_avg))
