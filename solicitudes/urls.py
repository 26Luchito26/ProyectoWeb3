from django.urls import path
from . import views

urlpatterns = [
    path('solicitudes_retiro/', views.solicitudes_retiro, name="Solicitudes_Retiro"),
    path('solicitudes_tolva/', views.solicitudes_tolva, name="Solicitudes_Tolva"),
    path('solicitudes_epps/', views.solicitudes_epps, name="Solicitudes_Epps"),
    path('exportar_solicitudes_csv/', views.exportar_solicitudes_excel, name="exportar_solicitudes_excel"),
]