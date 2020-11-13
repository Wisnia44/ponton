from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views
from .views import ServerUpdateView, GetServiceView

urlpatterns = [
	path('service/<int:pk>/', GetServiceView.as_view(), name='get-service-api'),
	path('server/<int:pk>/', ServerUpdateView.as_view(), name='server-update-api'),
	path('auth-get-token/', views.obtain_auth_token, name='get-token'),
]
