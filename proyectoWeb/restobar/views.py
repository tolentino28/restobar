from django.shortcuts import render, redirect
from .models import Carta, Galeria
from .forms import ContactoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def carta(request):
    carta_items = Carta.objects.all()
    return render(request, 'carta.html', {'carta_items': carta_items})


def contactenos(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = ContactoForm()
    return render(request, 'contactenos.html', {'form': form})


def gracias_view(request):
    return render(request, 'gracias.html')

from django.shortcuts import render
from .models import Galeria

def galeria(request):
    imagenes = Galeria.objects.filter(imagen__isnull=False)
    videos = Galeria.objects.filter(video__isnull=False)
    return render(request, 'galeria.html', {'imagenes': imagenes, 'videos': videos})


def nosotros(request):
    return render(request, 'nosotros.html')

from django.shortcuts import redirect
from .models import Registro
#from django.http import HttpResponse
# Create your views here.
@login_required
def formularioInicio(request):
    mensaje = ''
    if request.method == 'POST':
        formNombre = request.POST.get('name')
        formTelefono = request.POST.get('phone')
        formCorreo = request.POST.get('email')
        formFecha = request.POST.get('date')
        formHora = request.POST.get('time')
        formMensaje = request.POST.get('message')

        insertarRegistro = Registro(
            nombre=formNombre,
            telefono=formTelefono,
            correo=formCorreo,
            fecha=formFecha,
            hora=formHora,
            contenido=formMensaje
        )
        insertarRegistro.save()
                
        mensaje = "Reserva agregada exitosamente."

    return render(request, 'reservas.html', {'mensaje': mensaje})
                
        # Redirigir a la página de inicio o a otra página de confirmación
        #return redirect('index')  # Asegúrate de tener una URL llamada 'home'
    
    # Si el método no es POST, renderiza la página con el formulario
    #return render(request, 'reservas.html')

    #ADMIN/user:admin/password:admin
def cancelar_reserva(request):
    mensaje = ''
    if request.method == 'POST':
        cancel_nombre = request.POST.get('cancel_name')
        try:
            reserva = Registro.objects.get(nombre=cancel_nombre)
            reserva.delete()
            mensaje = "Reserva cancelada exitosamente."
        except Registro.DoesNotExist:
            mensaje = "No se encontró una reserva con ese nombre."

    return render(request, 'reservas.html', {'mensaje': mensaje})
from django.contrib.auth.models import User
from django.contrib.auth import login 
from django.contrib.auth import logout


# -------------------------------------------------------------------------------
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import cliente
from django.contrib import messages

def crearUsuario(request):
    if request.method == "POST":
        formUsuario = request.POST.get("nuevoCliente")
        formPassword = request.POST.get("nuevaClave")
        if User.objects.filter(username=formUsuario).exists():
            messages.error(request, "El nombre de usuario ya existe. Por favor, elija otro.")
            return render(request, "registrar.html")
        else:
            insertarCliente = User.objects.create_user(username=formUsuario, password=formPassword)
            if insertarCliente is not None:
                login(request, insertarCliente)
                return redirect("completarPerfil")
    return render(request, "registrar.html")

@login_required
def completarPerfil(request):
    if request.method == "POST":
        dni = request.POST.get("dni")
        telefono = request.POST.get("telefono")
        direccion = request.POST.get("direccion")
        cliente.objects.create(usuario=request.user, dni=dni, telefono=telefono, direccion=direccion)
        return redirect("cuentaCliente")
    return render(request, "cliente.html")

@login_required
def cuentaCliente(request):
    return render(request, 'dashboard.html')

def salirUsuario(request):
    logout(request)
    return redirect("index")

def vistaLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("cuentaCliente")
    return render(request, "login.html")
