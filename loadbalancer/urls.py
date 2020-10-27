from django.urls import path

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
    WelcomeView,
    AnonymousUserView,
    NotOwnerView,
)

#app_name = 'loadbalancer'
urlpatterns = [
    #User based views
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('user-update/', UserUpdateView.as_view(), name='user-update'),
    path('user-delete/', UserDeleteView.as_view(), name='user-delete'),
    path('user-change-password/', UserChangePassword.as_view(), name='change-password'),

    #Main views
    path('', WelcomeView.as_view(), name='welcome'),
    path('home/', HomeView.as_view(), name='home'),
    path('anonymous-user/', AnonymousUserView.as_view(), name='anonymous-user'),
    path('not-owner/', NotOwnerView.as_view(), name='not-owner'),
]