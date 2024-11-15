from django.contrib import admin
from .models import Proyect,Task
# panel de admin que nos permite administrar todas las aplicaciones, crear datos, definir permisos, etc
# aca añadimos para el panel de admin
admin.site.register(Proyect)
admin.site.register(Task)
