from django.urls import path
from . import views

app_name = 'portefolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('projetoscurso', views.projetoscurso_page_view, name='projetocurso'),
    path('projetospessoais', views.projetospessoais_page_view, name='projetospessoais'),
    path('projetosescola', views.projetosescola_page_view, name='projetosescola'),
    path('sobre', views.sobre_page_view, name='sobre')

]