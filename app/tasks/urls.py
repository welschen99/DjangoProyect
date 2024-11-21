from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('protected/', login_required(views.protected_view), name='protected'),
    # path('', views.post_list, name='post_list'),
    path('hello/<str:username>', views.hello),
    # path('proyects', views.proyects),
    # path('task<int:id>', views.proyects),
    path('', views.task_list, name='task_list'),
    path('tarea/<int:pk>/', views.task_detail, name='task_detail'),
    path('tarea/create/', views.task_create, name='task_create'),
    path('tarea/edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('tarea/delete/<int:pk>/', views.task_delete, name='task_delete'),
]