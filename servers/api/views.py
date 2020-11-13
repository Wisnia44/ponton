from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ServerSerializer
from servers.models import Server, Service
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from servers.balancing_algs import round_robin, min_ping, min_cpu_usage

class ServerUpdateView (generics.UpdateAPIView):
	lookup_field = 'pk'
	serializer_class = ServerSerializer

	def get_queryset(self):
		return Server.objects.all()
	
	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}

class GetServiceView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
            if service.algorithm == 'round_robin':
            	address = round_robin(service)
            elif service.algorithm == 'lowest_ping_time':
            	address = min_ping(service)
            elif service.algorithm == 'lowest_cpu_usage':
            	address = min_cpu_usage(service)
            
            response = HttpResponse("Redirection")
            response["Location"] = address
            return response
            #return Response(content, status=status.HTTP_302_FOUND, LOCATION:address)

        except Service.DoesNotExist:
            raise Http404
