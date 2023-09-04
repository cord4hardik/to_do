from django.urls import path
from .views import (
    UserListAPIView, 
    UserDetailAPIView,
    UserLoginAPIView,
    UserLogoutView,
    )

# created customized urls for the functionality of accounts
urlpatterns = [
    path('register-user/', UserListAPIView.as_view(), name='user-register'),
    path('register-user/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('logout/',UserLogoutView.as_view(), name='user-logout'),
    

]

