from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informacion_laboratorios/', views.informacion_laboratorios, name='informacion_laboratorios'), 
    path('agregar_laboratorio/', views.agregar_laboratorio, name='agregar_laboratorio'), 
    path('editar_laboratorio/<int:laboratorio_id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar_laboratorio/<int:laboratorio_id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
    path('ingresar_usuario/', views.ingresar_usuario, name='ingresar_usuario'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='logout'),
]