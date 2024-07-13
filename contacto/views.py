from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage


def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST) # Cargamos en nuestro formulario los datos para rescatarlos.
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde Coca Cola Andina - Resiter", 
            "El usuario con nombre {} con la dirección {} te escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["pruebacocacolaandinaresiter@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})