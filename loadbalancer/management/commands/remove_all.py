from django.core.management.base import BaseCommand
from servers.models import Server, Service

class Command(BaseCommand):

    def handle(self, *args, **options):
        services = Service.objects.all()
        servers = Server.objects.all()

        servers.delete()
        services.delete()
