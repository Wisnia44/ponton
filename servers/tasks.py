from celery import shared_task
from .models import Server, Service
from .funcs import ping_time

@shared_task
def count_servers():
	return Server.objects.count

@shared_task(name='ping_servers')
def ping_servers():
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
			server.ping_time = rtt_avg
			server.save()
