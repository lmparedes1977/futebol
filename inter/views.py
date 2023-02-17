from django.shortcuts import render

from utils.trofeus.fabrica import cria_vitoria

lista_vitorias = [cria_vitoria() for _ in range(5)]

responsaveis = {'pessoas': [{'nome': 'Abilio dos Reis'},
                            {'nome': 'Manga'}, {'nome': 'Bigorna'}]}


def home(req):
    """Doc"""
    return render(req, 'inter/paginas/home.html')


def sobre(req):
    """Doc"""
    return render(req, 'inter/paginas/sobre.html')


def contato(req):
    """Doc"""
    return render(req, 'inter/paginas/contato.html', context=responsaveis)


def trofeus(req):
    """Doc"""
    return render(req, 'inter/paginas/trofeus.html', context={'lista': lista_vitorias})


def trofeu(req, id):
    """Doc"""
    for item in lista_vitorias:
        if item['ano'] == id:
            venceu = item
            break
    return render(req, 'inter/paginas/trofeu.html', context={'campeonato_vencido': venceu})
