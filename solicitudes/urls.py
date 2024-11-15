from django.urls import path
from . import views

urlpatterns = [
    path('solicitudes_retiro/', views.solicitudes_retiro, name="Solicitudes_Retiro"),
    path('solicitudes_tolva/', views.solicitudes_tolva, name="Solicitudes_Tolva"),
    path('solicitudes_epps/', views.solicitudes_epps, name="Solicitudes_Epps"),
    path('exportar_solicitudes_csv/', views.exportar_solicitudes_excel, name="exportar_solicitudes_excel"),

    # Route for deleting a solicitud (request)
    path('solicitud/eliminar/<int:solicitud_id>/<str:tipo_solicitud>/', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('editar_solicitud/<int:solicitud_id>/<str:tipo_solicitud>/', views.editar_solicitud, name='editar_solicitud'),
]
