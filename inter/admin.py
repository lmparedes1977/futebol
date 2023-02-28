from django.contrib import admin

from .models import Campeonato, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    """Doc"""
    # adicionaremos mais coisa aqui depois, por hora, pode ficar vazio


admin.site.register(Categoria, CategoriaAdmin)


# esta é outra forma de fazer usando decorators
@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    """Doc"""
