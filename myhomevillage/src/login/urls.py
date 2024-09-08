from django.urls import path
from .views import loginreg, register

urlpatterns = [
    path('', loginreg, name='login-register'),
    path('register/', register, name='register'),
]
