from django.shortcuts import render

# Create your views here.
import requests

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .models import Address

class AddressView(CreateView):

    model = Address
    fields = ['address']
    template_name = 'Search.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoiY29ucmFkZ2FiZSIsImEiOiJjbDYxd2p3NjUwOHRsM2JteGVtbnExYmQ2In0.Ac3WHsw3rADEtNYnauAfYw'
        context['addresses'] = Address.objects.all()
        return context