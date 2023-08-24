from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('<str:slug>/', Test.as_view(), name='test'),
]