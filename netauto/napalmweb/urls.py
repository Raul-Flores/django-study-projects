from django.urls import path
from napalmweb import views

urlpatterns = [
    path('', views.home, name='home'),
]