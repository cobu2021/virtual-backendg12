"""agenda URL Configuration

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
from django.urls import path , include
#include >sirve para incluir un archivo con varias rutas al archivo
#de rutas del proyecto
from django.conf.urls.static import static
# se pueden utilizar todas las variables definidas en el archivo SETTINGS del proyecto
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls'))
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
# el metodo static sirve para retornar una lista de URLPatterns pero que
#establecere que archivos y que rutas retornaran
