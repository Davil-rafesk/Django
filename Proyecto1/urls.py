"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Proyecto1.views import dame_fecha, saludo, despedida, calcula_edad, plantillas, plantillasDos

# <int:agno> es la forma en la que se le pasa un parámetro a unUL, de esta manera se puede hace una página dinámica.
# <int:edad>/<int:agno> se usa para pasarle 2 parámetros a la URL, ej: http://localhost:8000/edades/50/2036


urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo),
    path("despedida/", despedida),
    path("fecha/", dame_fecha),
    path("edades/<int:edad>/<int:agno>", calcula_edad),
    path("plantillas/", plantillas),
    path("plantillasDos/", plantillasDos)
]
