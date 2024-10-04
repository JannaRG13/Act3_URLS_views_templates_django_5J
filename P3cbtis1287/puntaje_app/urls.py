from django.urls import path
from . import views 
urlpatterns = [
    path("",views.index,name="index"),
    path("agencia/",views.agencia,name="agencia"),
    path("cliente/",views.cliente,name="cliente"),
    path("empleado/",views.empleado,name="empleado"),
    path("vehiculo/",views.vehiculo,name="vehiculo")
    
]
