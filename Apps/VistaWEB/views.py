from django.shortcuts import render, redirect
from django.http import HttpResponse

from Apps.NoticiasCRUD.models import NoticiasModelo

def home(request):

    return render(request, 'home.html')

#def noticias_mostrar(request, tipo):
def noticias_mostrar(request):
    #datos = NoticiasModelo.objects.filter(tipo=tipo)
    datos = NoticiasModelo.objects.filter(tipo='N')
    contexto = {'lista': datos}
    return render(request, 'noticias.html', contexto)

def eventos_mostrar(request):
    datos = NoticiasModelo.objects.filter(tipo='E')
    contexto = {'lista': datos}
    return render(request, 'eventos.html', contexto)

def detalle(request, id):
    item = NoticiasModelo.objects.get(id = id)
    return render(request, 'detalle.html', {'item': item})
