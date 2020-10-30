from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import (
    #User based views
    UserLoginView,
    UserLogoutView,
    UserSignupView,
    UserDeleteView,
    UserUpdateView,
    UserChangePassword,

    #Main views
    HomeView,
)

#app_name = 'loadbalancer'
urlpatterns = [
    # User based views
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('user-update/', UserUpdateView.as_view(), name='user-update'),
    path('user-delete/', UserDeleteView.as_view(), name='user-delete'),
    path('user-change-password/', UserChangePassword.as_view(), name='change-password'),

    # Main views
    path('home/', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='index'),

    # Default views
    url('^', include('django.contrib.auth.urls')),
]
