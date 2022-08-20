from django.urls import path
from . import views

app_name = 'RenagerBackend_App'

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.AddressView.as_view(), name='Search')
]