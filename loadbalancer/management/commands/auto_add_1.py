from django.core.management.base import BaseCommand
from servers.models import Server, Service
from django.contrib.auth.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('no_services', type=int)
        parser.add_argument('no_servers', type=int)

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            username='testuser',
            password='WzkW49JLNNEave9',
            )

        number_of_services = options['no_services']
        number_of_servers = options['no_servers']

        for i in range(0, number_of_services):
            # create service Y for user X
            name = "Usluga_" + str(i)
            service = Service.objects.create(owner=user, algorithm='lowest_ping_time', name=name)
            for j in range(0, number_of_servers):
                #create servers for service Y
                if j%3==0:
                    server = Server.objects.create(address='google.com', service=service)
                elif j%3==1:
                    server = Server.objects.create(address='facebook.com', service=service)
                else:
                    server = Server.objects.create(address='bing.com', service=service)

        print("{} services have been created. For each of them {} servers have been created".format(number_of_services, number_of_servers))
        print("{} servers have been created in total".format(number_of_services*number_of_servers))
