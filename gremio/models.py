from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    """Doc"""
    titulo = models.CharField(max_length=120)

    def __str__(self) -> str:
        """Doc"""
        return str(self.titulo)


class Campeonato(models.Model):
    """Doc"""
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    slug = models.SlugField()
    ano_campeao = models.DateField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to='imagens/%Y/%m/%d/', null=True)

    def __str__(self) -> str:
        """Doc"""
        return f'{self.titulo} - {self.ano_campeao}'
