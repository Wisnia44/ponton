from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ServerSerializer
from servers.models import Server, Service

class ServerUpdateView (generics.UpdateAPIView):
	lookup_field = 'pk'
	serializer_class = ServerSerializer

	def get_queryset(self):
		return Server.objects.all()
	
	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}

class GetService(APIView):
    def get_object(self, pk):
        pass

    def get(self, request, pk, format=None):
    	pass