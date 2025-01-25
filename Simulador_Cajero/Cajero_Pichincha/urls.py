from django.urls import path
from . import views
app_name = 'Cajero_Pichincha'

urlpatterns = [
    path("", views.index, name="index"),
]