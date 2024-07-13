from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Index"),
    path('bloqueado/', views.bloqueado, name="Bloqueado"),
   
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Nos muestra los datos guardados en media desde el navegador.
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Nos muestra los datos guardados en media desde el navegador.