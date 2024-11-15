from django.conf import settings
from django.db import models
from django.utils import timezone


class Proyect(models.Model):
    #el id por defecto django se lo agrega

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
    title=models.CharField(max_length=200)
    description=models.TextField()
    # Para decirle que cada tarea va a pertenecer a un proyecto, con su respectivo id
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE) #on_delete -> que queremos que haga con la tarea cuando se elimine un proyecto. El tipo cascada es que cuando se elimina el proyecto, se eliminan todas las tareas relacionadas a ese proyecto

    def __str__(self):
        return self.title + ' - ' + self.proyect.title
