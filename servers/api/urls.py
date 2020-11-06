from django.conf.urls import url
from .views import ServerUpdateView

app_name = 'api'
urlpatterns = [
	url(r'^(?P<pk>\d+)/$', ServerUpdateView.as_view(), name='api-server-update'),
]