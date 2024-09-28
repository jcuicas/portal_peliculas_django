from django.shortcuts import render
from .services import genero_peliculas, ver_peliculas

# Create your views here.
def inicio(request):
    parametros = {
        'genres': '28',
        'page': '1',
    }
    
    datos = {
        'titulo': 'Portal de peliculas',
        'encabezado': 'Lista de peliculas',
        'generos': genero_peliculas(),
        'peliculas': ver_peliculas(parametros),
        'images': 'https://image.tmdb.org/t/p/w300/',
    }
    
    return render(request, 'peliculas/index.html', datos)