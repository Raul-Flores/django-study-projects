from collections import namedtuple
from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _
from .models import netdevice


class deviceForm(forms.ModelForm):
    class Meta:
        model = netdevice
        fields = ('direccionip', 'usuario', 'protocolo', 'puerto', 'password')
        labels = {
            'direccionip': _('Direccion IP'),
            'protocolo': _('Protocolo de comunicacion'),
            'puerto': _('No. Puerto'),
            'usuario': _('Username'),
            'password': _('Password') }
        widgets = {
            'password': forms.PasswordInput(),    
        }