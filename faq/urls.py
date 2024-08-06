from django.urls import path

from . import views

urlpatterns = [
    path('online-customer-service/', views.online_server, name='online_server'),
    path('questions/', views.questions, name='questions'),
]