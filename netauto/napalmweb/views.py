from django.shortcuts import render, redirect
from napalmweb.models import netdevice
from napalmweb.forms import deviceForm
from netmiko import ConnectHandler
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
#def home(request):
#    devices = netdevice.objects.all()
#    print (devices)
#    form = deviceForm()
#    contexto = {
#        'form': form
#    }
#    return render(request, 'base_app.html', contexto)

#### CRUD Sencillo #######
@login_required
def home(request):
    devices = netdevice.objects.all()
    print (devices)
    if request.method == 'GET':
        form = deviceForm()
        contexto = {
          'form':form,
          'device': devices
        }
    else:
        form = deviceForm(request.POST)
        contexto = {
          'form':form,
          'device': devices
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'base_app.html', contexto)

@login_required
def listado(request):
    devices = netdevice.objects.all()
    print (devices)
    if request.method == 'GET':
        form = deviceForm()
        contexto = {
          'form':form,
          'device': devices
        }
    else:
        form = deviceForm(request.POST)
        contexto = {
          'form':form,
          'device': devices
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'listado_equipos.html', contexto)

@login_required
def editarDispositivo(request,id):
    devices = netdevice.objects.get(id = id)
    if request.method =='GET':
        form = deviceForm(instance = devices)
        contexto = {
            'form': form
        }
    else:
        form = deviceForm(request.POST, instance = devices)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base_app.html', contexto)
        
@login_required
def eliminarDispositivo(request, id):
    devices = netdevice.objects.get(id = id)
    devices.delete()
    return redirect('home')
    
@login_required
def comandos(request,id):
    devices = netdevice.objects.get(id = id)
    if request.method == 'GET':
        contexto = {
          'device': devices
        }
    else:
        device = {
            'username': devices.usuario, 
            'ip': devices.direccionip, 
            'device_type': 'cisco_ios',
            'port': devices.puerto,
            'password': devices.password
            }
        try:          
            connection = ConnectHandler(**device)
            resultado = connection.send_command(request.POST['comando'], use_textfsm=True)
        except Exception as error:
            resultado = error
        contexto = {
          'device': devices,
          'resultado': resultado
        }
    return render(request, 'comandos.html', contexto)