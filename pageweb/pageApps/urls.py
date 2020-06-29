from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('client/<id_client>', views.view_client),
]
