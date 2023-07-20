"""DJANGO_TALLER_FINAL URL Configuration

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
from Django_taller_final_app.views import index, guardar, verPartipantes, ParticipanteList, ParticipanteDetalle, participante_list, participante_detalle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('guardar/', guardar),
    path('participantes/', verPartipantes),
    path('clase/', ParticipanteList.as_view()),
    path('clase/<int:pk>/', ParticipanteDetalle.as_view()),
    path('funcion/', participante_list),
    path('funcion/<int:id>', participante_detalle )


]   
