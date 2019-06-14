from django.shortcuts import render, redirect
from django.http import HttpResponse

from Apps.NoticiasCRUD.models import NoticiasModelo
from Apps.NoticiasCRUD.forms import NoticiasCrearForm

def noticias_listar(request):
    datos = NoticiasModelo.objects.all()
    contexto = {'lista': datos}
    return render(request, 'noticias_listar.html', contexto)


def noticias_crear(request):
    if request.method == "POST":
        form = NoticiasCrearForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('noticias_listar')
    else:
        form=NoticiasCrearForm()

    contexto = {'form': form}
    return render(request, 'noticias_crear.html', contexto)



def noticias_eliminar(request, id):

    noticia = NoticiasModelo.objects.get(id = id)
    if request.method == "POST":
        noticia.delete()
        return redirect('noticias_listar')
    else:
        return render(request, 'noticias_eliminar.html', {'noticia': noticia})



def noticias_editar(request, id):

    noticia = NoticiasModelo.objects.get(id = id)
    if request.method == "GET":
        form=NoticiasCrearForm(instance=noticia)
    else:
        form=NoticiasCrearForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias_listar')
    contexto = {'form': form}
    return render(request, 'noticias_editar.html', contexto)