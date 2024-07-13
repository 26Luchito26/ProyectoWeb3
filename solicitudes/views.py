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
    
    solicitudes_retiro = Solicitudes_Retiro.objects.filter(id_usuario=request.user)
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
    
    solicitudes_epps = Solicitudes_Epps.objects.filter(id_usuario=request.user)
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
    
    solicitudes_tolva = Solicitudes_Tolva.objects.filter(id_usuario=request.user)
    return render(request, "solicitudes/solicitudes_tolva.html", {"solicitudes_tolva": solicitudes_tolva, "form": form})

@login_required(login_url='Bloqueado')
def exportar_solicitudes_excel(request):
    solicitudes_retiro = Solicitudes_Retiro.objects.filter(id_usuario=request.user)
    solicitudes_epps = Solicitudes_Epps.objects.filter(id_usuario=request.user)
    solicitudes_tolva = Solicitudes_Tolva.objects.filter(id_usuario=request.user)

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
