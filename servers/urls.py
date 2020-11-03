from django.urls import path
from .views import (
	# service based views
	ServiceCreateView,
	ServiceDetailView,
	ServiceUpdateView,
	ServiceDeleteView,
	ServiceListView,

	# server based views
	ServerCreateView,
	ServerDetailView,
	ServerUpdateView,
	ServerDeleteView,
	ServerListView
	)
# app_name = 'servers'
urlpatterns = [
	# service based views
    path('service/create/', ServiceCreateView.as_view(), name='service-create'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('services/', ServiceListView.as_view(), name='service-list'),

    # server based views
    path('service/<int:pk>/server/create/', ServerCreateView.as_view(), name='server-create'),
    path('service/<int:pk1>/server/<int:pk2>/', ServerDetailView.as_view(), name='server'),
    path('service/<int:pk1>/server/<int:pk2>/update/', ServerUpdateView.as_view(), name='server-update'),
    path('service/<int:pk1>/server/<int:pk2>/delete/', ServerDeleteView.as_view(), name='server-delete'),
    path('service/<int:pk>/servers/', ServerListView.as_view(), name='server-list'),
    
    # api view
    #path('service/<int:pk>/api', ServiceApiView.as_view(), name='service-api'),
]
