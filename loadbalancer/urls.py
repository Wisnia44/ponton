from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import (
    #User based views
    UserLogoutView,
    UserSignupView,
    UserSignupView2,
    UserDeleteView,
    UserUpdateView,
    UserChangePassword,
    UserUnloggedView,

    #Main views
    HomeView,
    HelpView
)

#app_name = 'loadbalancer'
urlpatterns = [
    # User based views
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('signup2/', UserSignupView2.as_view(), name='signup2'),
    path('user-update/', UserUpdateView.as_view(), name='user-update'),
    path('user-delete/', UserDeleteView.as_view(), name='user-delete'),
    path('user-change-password/', UserChangePassword.as_view(), name='change-password'),
    path('unlogged/', UserUnloggedView.as_view(), name='unlogged'),

    # Main views
    path('home/', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='index'),
    path('help/', HelpView.as_view(), name='help'),

    # Default views
    url('^', include('django.contrib.auth.urls')),
]
