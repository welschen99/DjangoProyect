from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Proyect,Task
from django.shortcuts import get_object_or_404 #devuelve una pagina 404 si no encuentra
def post_list(request):
    return render(request, 'blog/blog.html', {})

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