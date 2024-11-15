from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PerfilForm
from .models import Perfil

@login_required
def perfil_view(request):
    try:
        perfil = request.user.perfil
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(usuario=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            # Actualizar datos del usuario
            usuario = request.user
            usuario.username = form.cleaned_data['username']
            usuario.first_name = form.cleaned_data['first_name']
            usuario.last_name = form.cleaned_data['last_name']
            usuario.save()
            
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    
    return render(request, 'perfil/perfil.html', {
        'form': form,
        'perfil': perfil
    })
