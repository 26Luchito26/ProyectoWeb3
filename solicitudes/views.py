from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Solicitudes_Epps, Solicitudes_Retiro, Solicitudes_Tolva
from .forms import SolicitudEppsForm, SolicitudRetiroForm, SolicitudTolvaForm
from django.http import HttpResponse
from openpyxl import Workbook
from django.contrib import messages

@login_required(login_url='Bloqueado')
def solicitudes_retiro(request):
    if request.method == 'POST':
        form = SolicitudRetiroForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.id_usuario = request.user
            solicitud.tipo_usuario = request.user.tipo_usuario
            solicitud.save()
            messages.success(request, 'Solicitud de Retiro enviada correctamente.')
            return redirect('Solicitudes_Retiro')
    else:
        form = SolicitudRetiroForm()
    
    solicitudes_retiro = Solicitudes_Retiro.objects.all()  # Cambiado de id_usuario=request.user
    return render(request, "solicitudes/solicitudes_retiro.html", {"solicitudes_retiro": solicitudes_retiro, "form": form})


@login_required(login_url='Bloqueado')
def solicitudes_epps(request):
    if request.method == 'POST':
        form = SolicitudEppsForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.id_usuario = request.user
            solicitud.tipo_usuario = request.user.tipo_usuario
            solicitud.save()
            messages.success(request, 'Solicitud de EPPs enviada correctamente.')
            return redirect('Solicitudes_Epps')
    else:
        form = SolicitudEppsForm()
    
    solicitudes_epps = Solicitudes_Epps.objects.all()  # Cambiado de id_usuario=request.user
    return render(request, "solicitudes/solicitudes_epps.html", {"solicitudes_epps": solicitudes_epps, "form": form})


@login_required(login_url='Bloqueado')
def solicitudes_tolva(request):
    if request.method == 'POST':
        form = SolicitudTolvaForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.id_usuario = request.user
            solicitud.tipo_usuario = request.user.tipo_usuario
            solicitud.save()
            messages.success(request, 'Solicitud de Tolva enviada correctamente.')
            return redirect('Solicitudes_Tolva')
    else:
        form = SolicitudTolvaForm()
    
    solicitudes_tolva = Solicitudes_Tolva.objects.all()  # Cambiado de id_usuario=request.user
    return render(request, "solicitudes/solicitudes_tolva.html", {"solicitudes_tolva": solicitudes_tolva, "form": form})


@login_required(login_url='Bloqueado')
def exportar_solicitudes_excel(request):
    solicitudes_retiro = Solicitudes_Retiro.objects.all()  # Cambiado de id_usuario=request.user
    solicitudes_epps = Solicitudes_Epps.objects.all()      # Cambiado de id_usuario=request.user
    solicitudes_tolva = Solicitudes_Tolva.objects.all()    # Cambiado de id_usuario=request.user

    filename = 'exportar_solicitudes.xlsx'

    wb = Workbook()
    ws = wb.active
    ws.title = "Solicitudes"

    ws.append(['Usuario', 'Nombre', 'Apellido', 'RUT', 'Tipo de Solicitud', 'Fecha de Emisión', 'Descripción', 'Cantidad', 'Tipo de Material', 'Patente'])

    for solicitud in solicitudes_retiro:
        fecha_realizacion = solicitud.fecha_realizarR.strftime('%Y-%m-%d') if solicitud.fecha_realizarR else ''
        ws.append([
            solicitud.id_usuario.username,
            solicitud.id_usuario.first_name,
            solicitud.id_usuario.last_name,
            solicitud.id_usuario.rut,
            'Solicitud de Retiro',
            fecha_realizacion,
            solicitud.descripcionRetiro,
            solicitud.cantidadRetiro,
            solicitud.tipo_materialRetiro,
            solicitud.patente,
        ])

    for solicitud in solicitudes_epps:
        fecha_realizacion = solicitud.fecha_realizarEP.strftime('%Y-%m-%d') if solicitud.fecha_realizarEP else ''
        ws.append([
            solicitud.id_usuario.username,
            solicitud.id_usuario.first_name,
            solicitud.id_usuario.last_name,
            solicitud.id_usuario.rut,
            'Solicitud de EPPs',
            fecha_realizacion,
            solicitud.descripcionEpps,
            '',  # Ajusta según los campos específicos de Solicitudes_Epps
            solicitud.tipo_materialEpps,
            '',  # Ajusta según los campos específicos de Solicitudes_Epps
        ])

    for solicitud in solicitudes_tolva:
        fecha_realizacion = solicitud.fecha_realizarT.strftime('%Y-%m-%d') if solicitud.fecha_realizarT else ''
        ws.append([
            solicitud.id_usuario.username,
            solicitud.id_usuario.first_name,
            solicitud.id_usuario.last_name,
            solicitud.id_usuario.rut,
            'Solicitud de Tolva',
            fecha_realizacion,
            solicitud.descripcionTolva,
            '',  # Ajusta según los campos específicos de Solicitudes_Tolva
            '',  # Ajusta según los campos específicos de Solicitudes_Tolva
            '',  # Ajusta según los campos específicos de Solicitudes_Tolva
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    wb.save(response)
    return response

#########################################################################################################################
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Solicitudes_Epps, Solicitudes_Retiro, Solicitudes_Tolva

@login_required(login_url='Bloqueado')
def eliminar_solicitud(request, solicitud_id, tipo_solicitud):
    # Selecciona el modelo correcto según el tipo de solicitud
    if tipo_solicitud == 'epps':
        solicitud = get_object_or_404(Solicitudes_Epps, id_solicitudEpps=solicitud_id)
    elif tipo_solicitud == 'retiro':
        solicitud = get_object_or_404(Solicitudes_Retiro, id_solicitudRetiro=solicitud_id)
    elif tipo_solicitud == 'tolva':
        solicitud = get_object_or_404(Solicitudes_Tolva, id_solicitudTolva=solicitud_id)
    else:
        messages.error(request, 'Tipo de solicitud no válido.')
        return redirect('panel_trabajador')  # Ajusta según tu lógica de redirección

    # Verifica si el usuario es jefe o dueño de la solicitud
    if request.user.tipo_usuario == Usuario_Registro.TIPO_USUARIO_JEFE:  # Uso del valor desde las constantes
        # Los jefes pueden eliminar solicitudes de cualquier usuario
        solicitud.delete()
        messages.success(request, 'Solicitud eliminada exitosamente.')
    elif solicitud.id_usuario == request.user:
        # Los trabajadores solo pueden eliminar sus propias solicitudes
        solicitud.delete()
        messages.success(request, 'Solicitud eliminada exitosamente.')
    else:
        messages.error(request, 'No tienes permiso para eliminar esta solicitud.')

    # Depuración: imprime el tipo de usuario en consola para confirmar el valor
    print(f"Tipo de usuario: {request.user.tipo_usuario}")  # O puedes usar logging.debug

    # Redirecciona según el tipo de usuario
    if request.user.tipo_usuario == Usuario_Registro.TIPO_USUARIO_JEFE:
        return redirect('panel_jefe')
    else:
        return redirect('panel_trabajador')


from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Solicitudes_Epps, Solicitudes_Retiro, Solicitudes_Tolva, Usuario_Registro
from .forms import SolicitudEppsForm, SolicitudRetiroForm, SolicitudTolvaForm


def editar_solicitud(request, solicitud_id, tipo_solicitud):
    # Selecciona el modelo y el formulario correcto según el tipo de solicitud
    if tipo_solicitud == 'epps':
        solicitud = get_object_or_404(Solicitudes_Epps, id_solicitudEpps=solicitud_id)
        form = SolicitudEppsForm(instance=solicitud)
    elif tipo_solicitud == 'retiro':
        solicitud = get_object_or_404(Solicitudes_Retiro, id_solicitudRetiro=solicitud_id)
        form = SolicitudRetiroForm(instance=solicitud)
    elif tipo_solicitud == 'tolva':
        solicitud = get_object_or_404(Solicitudes_Tolva, id_solicitudTolva=solicitud_id)
        form = SolicitudTolvaForm(instance=solicitud)
    else:
        messages.error(request, 'Tipo de solicitud no válido.')
        return redirect('panel_trabajador')

    if request.method == 'POST':
        # Procesar el formulario con los datos enviados
        if tipo_solicitud == 'epps':
            form = SolicitudEppsForm(request.POST, instance=solicitud)
        elif tipo_solicitud == 'retiro':
            form = SolicitudRetiroForm(request.POST, instance=solicitud)
        elif tipo_solicitud == 'tolva':
            form = SolicitudTolvaForm(request.POST, instance=solicitud)

        # Verificar si el formulario es válido
        if form.is_valid():
            # Guardar los cambios en la solicitud, sin cambiar el usuario
            form.save()
            messages.success(request, 'Solicitud actualizada exitosamente.')
            return redirect('panel_jefe')  # O a donde necesites redirigir

    # Filtrar usuarios según el tipo de usuario logueado
    if request.user.tipo_usuario == 'jefe':
        # Los jefes pueden ver tanto a otros jefes como a trabajadores, excluyendo administradores
        usuarios = Usuario_Registro.objects.filter(tipo_usuario__in=['jefe', 'trabajador']).exclude(tipo_usuario='administrador')
    else:
        # Solo permitir que el trabajador vea a otros trabajadores
        usuarios = Usuario_Registro.objects.filter(tipo_usuario='trabajador')

    # Renderizar la plantilla con el formulario
    context = {
        'form': form,
        'tipo_solicitud': tipo_solicitud,
        'solicitud': solicitud,
        'usuarios': usuarios,  # Asegúrate de que esta lista está bien
    }
    return render(request, 'solicitudes/editar_solicitud.html', context)
