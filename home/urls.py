from django.urls import path

from gremio import views as gremio_view
from inter import views as inter_view

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home')
]
