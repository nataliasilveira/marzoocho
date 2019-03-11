"""salimossss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from iniciosalimos.views import cine_list, festi_list, crio_list, conamigos_list, enfmilia_list,ninos_list, paseos_list,turismo_list, airlib_list
from iniciosalimos.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('Cine', cine_list, name='Cinellama'),
    path('Festivales', festi_list, name='Festillama'),
    path('Criollas', crio_list, name='Criollama'),
    path('EnFamilia', enfmilia_list, name='familia'),
    path('Conamigos', conamigos_list, name='amigos'),
    path('ninos', ninos_list, name='ninos'),
    path('paseos', paseos_list, name='paseo'),
    path('Turismo', turismo_list, name='turi'),
    path('airelibre', airlib_list, name='aire'),

]
