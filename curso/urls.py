from django.conf.urls import url
from . import views

urlpatterns = [
    #url('', views.lista_peliculas, name ='lista_peliculas'),
    url('curso/nueva/', views.curso_nuevo, name='curso_nuevo'),
    ]