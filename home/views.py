from django.shortcuts import render


def home(req):
    """Doc"""
    return render(req, 'home/paginas/home.html')
