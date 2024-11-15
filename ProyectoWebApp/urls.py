from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('admin_panel/', views.admin_panel, name="admin_panel"),  # Admin Panel
    path('panel_administrativo_operacional/', views.panel_administrativo_operacional, name="panel_administrativo_operacional"),  # Admin Panel
    path('panel_trabajador/', views.panel_trabajador, name="panel_trabajador"),  # Trabajador Panel
    path('panel_jefe/', views.panel_jefe, name="panel_jefe"),  # Jefe Panel
]

# Serve media and static files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
