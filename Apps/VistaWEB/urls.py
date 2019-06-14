from django.urls import path, include

from Apps.VistaWEB.views import *


urlpatterns = [
    path('', home, name='home'),
    #con un parametro
    #path('noticias/<str:tipo>/', noticias_mostrar, name='noticias_mostrar'),
    path('noticias/', noticias_mostrar, name='noticias_mostrar'),
    path('eventos/', eventos_mostrar, name='eventos_mostrar'),
    path('detalle/<int:id>/', detalle, name='detalle'),
]
