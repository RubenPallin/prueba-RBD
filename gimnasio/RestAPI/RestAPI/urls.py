"""RestAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webserviceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classe', views.prueba_API),
    path('classes', views.obtener_listado_clases),
    path('orders/<int:idpersona>', views.obtener_listado_pedidos),
    path('calendar/<int:id_clase>', views.get_clases),
    path('calendar/<int:id_clase>', views.reserva_clases)
]
