from django.urls import path
from . import views
from .views import formularioInicio, cancelar_reserva
from .views import gracias_view
from .views import crearUsuario
from .views import salirUsuario
from .views import cuentaCliente

urlpatterns = [
    path('', views.index, name='index'),
    path('cartas/', views.carta, name='cartas'),
    path('contactenos/', views.contactenos, name='contactenos'),
    path('galeria/', views.galeria, name='galeria'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('reservas/', views.formularioInicio, name='reservas'),
    path('gracias/', gracias_view, name='gracias'),
    path('cancel_reserva/', cancelar_reserva, name='cancel_reserva'),
    path('nuevo-cliente/', views.crearUsuario, name='PaginaNuevoCliente'),
    path('logout/', views.salirUsuario, name='SalirCliente'),
    path('mi-dashboard/', views.cuentaCliente, name='cuentaCliente'),
    path('login/', views.vistaLogin, name='paginaLogin'),
    path('completar-perfil/', views.completarPerfil, name='completarPerfil'),
]
