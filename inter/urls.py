from django.urls import path

from . import views as inter_view

app_name = 'inter'

urlpatterns = [
    path('', inter_view.home, name='home'),
    path('sobre/', inter_view.sobre, name='sobre'),
    path('contato/', inter_view.contato, name='contato'),
    path('trofeus/', inter_view.trofeus, name='trofeus'),
    path('trofeus/trofeu/<int:id>', inter_view.trofeu, name='trofeu')
]
