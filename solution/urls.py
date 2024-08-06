from django.urls import path
from . import views

urlpatterns = [
    path('work-order-cost/', views.order_cost, name='order_cost'),
    path('real-time-cutiing-status/', views.real_time, name='real_time'),
    path('machine-utilization-status/',views.utilization, name='utilization'),
    path('shift-status', views.shift_status, name='shift_status'),
    path('workshop-bulletin-board/', views.workshop, name='workshop'),
    path('sawblade-predictive-diagnosis/', views.sawblade, name='sawblade'),
    path('real-time-app-notice/', views.real_time_app, name='real_time_app'),
    path('allowable-values-set-up/', views.allowable_values, name='allowable_values'),
    path('automatic-reports/', views.automatic_reports, name='automatic_reports'),
    path('sawlogix-app/', views.sawlogix, name='sawlogix'),
    path('more-solution/', views.more_solution, name='more_solution'),
]