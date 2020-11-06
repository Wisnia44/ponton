from .models import Server
from .funcs import ping_time

def ping_servers():
	servers = Server.objects.filter(analysis_method='ping')
	for server in servers:
		rtt_avg = ping_time(server.address)
		server.ping_time = rtt_avg
		server.save()

	print("ping_servers cron job")
