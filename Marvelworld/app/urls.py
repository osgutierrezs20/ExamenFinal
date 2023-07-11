from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('productos/', views.productos, name= "productos"),
    path('acerca-de/', views.acerca_de, name= "quienes_somos"),
    path('agregar-producto/', views.crear_producto, name="agregar_producto"),
    path('listar-productos/', views.listar_productos, name="listar_productos"),
    path('modificar-productos/<id>/', views.editar_producto, name="modificar_productos"),
    path('eliminar-productos/<id>/', views.eliminar_producto, name="eliminar_producto"),
    path('registro/', views.registro, name ="registro"),
]