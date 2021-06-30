from django.urls import path
from napalmweb import views

urlpatterns = [
    path('', views.home, name='home'),
    path('editarDispositivo/<int:id>/', views.editarDispositivo, name='editarDispositivo'),
    path('eliminarDispositivo/<int:id>/', views.eliminarDispositivo, name='eliminarDispositivo'),
]