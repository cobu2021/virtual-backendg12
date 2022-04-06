from django.urls import path
from .views import inicio

#seran todas las rutas de esta aoplicacion las Tendremos
urlpatterns = [
    path('inicio', inicio)
]
