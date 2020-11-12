from django.conf.urls import url
from django.urls import path
from .views import ServerUpdateView, GetServiceView

urlpatterns = [
	path('service/<int:pk>/', GetServiceView.as_view(), name='get-service-api'),
	path('server/<int:pk>/', ServerUpdateView.as_view(), name='server-update-api'),
]
