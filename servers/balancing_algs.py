from .models import Service, Server

def round_robin(service):
	queryset = Server.objects.filter(service=service.id)
	if service.last_round_server_id+1 < len(queryset):
		service.last_round_server_id += 1
	else:
		service.last_round_server_id = 0
	result = queryset[service.last_round_server_id].address
	#print(result)
	return result

def min_ping(service):
	queryset = Server.objects.filter(service=service.id)
	result_id = 0
	for i in range(0,len(queryset)):
		if queryset[i].ping_time < queryset[result_id].ping_time:
			result_id = i
	#print(queryset[result_id].address)
	return queryset[result_id].address

def min_cpu_usage(service):
	queryset = Server.objects.filter(service=service.id)
	result_id = 0
	for i in range(0,len(queryset)):
		if queryset[i].cpu_state < queryset[result_id].cpu_state:
			result_id = i
	return queryset[result_id].address
