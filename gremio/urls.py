from django.urls import path

from . import views as gremio_view

app_name = 'gremio'

urlpatterns = [
    path('', gremio_view.home, name='home'),
    path('sobre/', gremio_view.sobre, name='sobre'),
    path('contato/', gremio_view.contato, name='contato'),
    path('trofeus/', gremio_view.trofeus, name='trofeus'),
    path('trofeus/trofeu/<int:id>', gremio_view.trofeu, name='trofeu')
]
