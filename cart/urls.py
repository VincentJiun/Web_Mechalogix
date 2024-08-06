from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_item/<str:item_name>/', views.delete_item, name='delete_item'),
]