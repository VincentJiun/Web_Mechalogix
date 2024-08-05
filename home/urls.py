from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact-us/', views.contact, name='contact'),
    path('reward-points-redeem/', views.reward_points, name='reward_points'),
]