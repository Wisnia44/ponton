from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views
from .views import ServerUpdateView, GetServiceView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
	openapi.Info(
		title="Docs API",
		default_version='v1',
		description="API Documentation",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="contact@snippets.local"),
		license=openapi.License(name="BSD License"),
		),
	public=True,
	permission_classes=[permissions.AllowAny],
	)

urlpatterns = [
	path('service/<int:pk>/', GetServiceView.as_view(), name='get-service-api'),
	path('server/<int:pk>/', ServerUpdateView.as_view(), name='server-update-api'),
	path('auth-get-token/', views.obtain_auth_token, name='get-token'),
	url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
