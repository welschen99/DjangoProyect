from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Max


class Proyect(models.Model):
    #el id por defecto django se lo agrega
    codigo = models.CharField(max_length=11, unique=True, blank=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Task(models.Model):
    codigo = models.CharField(max_length=11, unique=True, blank=True )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE)
    # from django.contrib.auth.models import User
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='task/static/imagenes/', blank=True, null=True)  # Nuevo campo

    def set_Codigo(self):
        try:
            # Generar la parte inicial del código con el año actual
            codigo = 'TSK' + str(timezone.now().year) + '.'
            # Obtener el id máximo de las tareas existentes
            id_max = Task.objects.aggregate(Max('id'))['id__max']  # Esto obtiene el valor máximo del id
            # Si no hay ninguna tarea en la base de datos, empezar desde 0
            if id_max is None:
                id_max = 0
            # Formatear el id para que tenga 3 dígitos
            id_max = str(id_max + 1).zfill(3)  # Se asegura que tenga siempre 3 dígitos
            # Generar el código final
            codigoFinal = codigo + id_max
            self.codigo = codigoFinal
        except Exception as e:
            print(f"Error al generar el código: {e}")


    def __str__(self):
        return self.title + ' - ' + self.proyect.title


# TABLA EJEMPLO PARA RELACIONAR DE MUCHOS A MUCHOS

# class Comment(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')  # Relación a una tarea
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que hizo el comentario
#     content = models.TextField()  # Texto del comentario
#     created_at = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return f"Comment by {self.user.username} on {self.task.title}"