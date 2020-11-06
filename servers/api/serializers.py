from rest_framework import serializers
from servers.models import Server

class ServerSerializer(serializers.ModelSerializer):
	#url = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Server
		fields = [
			'pk',
			'cpu_state',
		]

	def get_url(self, obj):
		request = self.context.get("request")
		return obj.get_api_url(request=request)