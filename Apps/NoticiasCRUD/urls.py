from django.urls import path, include

from Apps.NoticiasCRUD.views import *


urlpatterns = [
    path('', noticias_listar, name='noticias_listar'),
    path('crear/', noticias_crear, name='noticias_crear'),
    path('eliminar/<int:id>/', noticias_eliminar, name='noticias_eliminar'),
    path('editar/<int:id>/', noticias_editar, name='noticias_editar'),
]