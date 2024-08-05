from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_home, name='product_home'),
    path('<str:slug>/', views.product_view, name='product_view'),
]