from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('hello/<str:username>', views.hello),
    path('proyects', views.proyects),
    path('task<int:id>', views.proyects),
]