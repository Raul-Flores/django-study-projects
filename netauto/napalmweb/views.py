from django.shortcuts import render, redirect
from napalmweb.models import netdevice
from napalmweb.forms import deviceForm
# Create your views here.
def home(request):
    devices = netdevice.objects.all()
    print (devices)
    form = deviceForm()
    contexto = {
        'form': form
    }
    return render(request, 'inventario.html', contexto)


