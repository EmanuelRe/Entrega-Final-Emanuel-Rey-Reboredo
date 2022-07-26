from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('porfolio', views.porfolio, name='porfolio'),
    path('administrar', views.administracion_Vista, name='administrar'),
    path('leerExperiencia', views.leer_Experiencia, name = "leerExperiencia"),
    path('buscar/', views.buscar_Experiencia),
    path('buscar/buscar/', views.buscar_Experiencia),
    path('eliminarExperiencia/<experiencia_titulo>/', views.eliminar_Experiencia, name="eliminarExperiencia"),
    path('editarExperiencia/<experiencia_titulo>/', views.editar_Experiencia, name="editarExperiencia"),
    path('administrar', views.CursoList.as_view(), name='administrar'),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='Porfolio/inicio.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    ]
