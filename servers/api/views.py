from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ServerSerializer
from servers.models import Server, Service
from django.http import Http404, HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required,login_required
from servers.balancing_algs import round_robin, min_ping, min_cpu_usage

class ServerUpdateView (generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,) 
    lookup_field = 'pk'
    serializer_class = ServerSerializer

    def put(self, request, pk, format=None):
        server = self.get_object()
        serializer = ServerSerializer(server, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Server.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def get_server(self, pk):
        # returns null if no match
        return Server.objects.filter(pk=pk).first() 

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
            service.request_counter += 1
            service.save()
            if 'http' not in address:
                address = 'http://' + address
            return HttpResponseRedirect(redirect_to=address)

        except Service.DoesNotExist:
            raise Http404
