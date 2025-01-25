from django.urls import path
from . import views
from .views import login_view, display_bank_services, register

app_name = 'Cajero_Pichincha'

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('display_bank_services', views.display_bank_services, name='display_bank_services'),
    path('register/', views.register, name='register')
]