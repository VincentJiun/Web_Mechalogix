from django.urls import path

from . import views

urlpatterns = [
    path('company/', views.company, name='company'),
    path('history/', views.history, name='history'),
    path('professional-team/', views.team, name='team'),
    path('product-advantages', views.product_advantages, name='product_advantages'),
    path('recruitment/', views.recruitment, name='recruitment'),
    path('news/', views.news, name='news'),
]