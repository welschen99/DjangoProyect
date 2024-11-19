from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import Proyect,Task
from django.shortcuts import get_object_or_404 #devuelve una pagina 404 si no encuentra
# from .forms import TaskForm

def post_list(request):
    return render(request, 'app/tasks/tasks.html', {})

def hello(request, username):
    print(username)
    return HttpResponse('<h2>Hello '+username +' </h2>')

def proyects(request):
    proyect = list(Proyect.objects.values())
    return JsonResponse(proyect, safe=False)

def task(request,id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task,id=id)
    return HttpResponse('tarea '+task.title)



def task_list(request):
    tareas = Task.objects.all()
    return render(request, 'task_list.html', {'tareas': tareas})


def task_detail(request, pk):
    tarea = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'tarea': tarea})

def task_create(request):
    projects = Proyect.objects.all()  # Obtiene todos los proyectos disponibles

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        proyect_id = request.POST.get('proyect')  # Asume que el ID del proyecto es pasado en el formulario

        if title and description and proyect_id:
            task = Task(
                title=title,
                description=description,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                proyect_id=proyect_id  # Relaciona la tarea con el proyecto
            )
            task.set_Codigo()
            task.save()
            return redirect('task_list')  # Redirige a la lista de tareas después de crear
    return render(request, 'task_create.html', {'projects': projects})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.proyect_id = request.POST.get('proyect')
        task.updated_at = timezone.now()
        task.save()
        return redirect('task_detail', pk=task.pk)  # Redirige a los detalles de la tarea después de editar

    return render(request, 'task_edit.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # Si el método de solicitud es POST, proceder a eliminar
    if request.method == 'POST':
        task.delete()
        # Redirige a la lista de tareas
        return redirect('task_list')

    # Si el método no es POST, solo muestra la página de confirmación
    return render(request, 'task_delete.html', {'task': task})