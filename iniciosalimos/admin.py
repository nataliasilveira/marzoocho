from django.contrib import admin
from .models import Funiciones, Categorias, Comentario, Lugares, Eventos, Edades, Departamentos


admin.site.register(Funiciones)
admin.site.register(Comentario)
admin.site.register(Categorias)
admin.site.register(Lugares)
admin.site.register(Eventos)
admin.site.register(Edades)
admin.site.register(Departamentos)
