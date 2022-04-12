from django.urls import path
from .views import  (EliminaArchivoApiView, EtiquetasApiView ,
                    inicio ,
                    PruebaApiView,
                    TareasApiView, 
                    TareaApiView,
                    ArchivosApiView)

#seran todas las rutas de esta aoplicacion las Tendremos
urlpatterns = [
    path('inicio', inicio),
    path('prueba',PruebaApiView.as_view()),
    path('tareas', TareasApiView.as_view()),
    path ('etiquetas',EtiquetasApiView.as_view()),
    path('tarea/<int:pk>',TareaApiView.as_view()),
    path('subir-imagen', ArchivosApiView.as_view()),
    path('eliminar-imagen',EliminaArchivoApiView.as_view())]
    

