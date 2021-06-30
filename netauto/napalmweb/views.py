from django.shortcuts import render, redirect
from napalmweb.models import netdevice
from napalmweb.forms import deviceForm
# Create your views here.
#def home(request):
#    devices = netdevice.objects.all()
#    print (devices)
#    form = deviceForm()
#    contexto = {
#        'form': form
#    }
#    return render(request, 'base_app.html', contexto)

#### CRUS Sencillo #######
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

def eliminarDispositivo(request, id):
    devices = netdevice.objects.get(id = id)
    devices.delete()
    return redirect('home')
