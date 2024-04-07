from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('balance/', views.balance, name='balance'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit/', views.deposit, name='deposit'),
]
