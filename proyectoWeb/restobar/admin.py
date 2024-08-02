from django.contrib import admin
from .models import Registro
from .models import Carta, Galeria
from .models import Contacto
from .models import cliente
# Register your models here.


admin.site.register(Registro)
admin.site.register(Carta)
admin.site.register(Galeria)
admin.site.register(Contacto)
admin.site.register(cliente)