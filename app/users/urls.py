"""Users URLs."""
from django.contrib.auth.views import LogoutView,LoginView
# Django
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_list, name='user_list'),  # Vista para el listado de usuarios
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),  # Vista para editar un usuario
]
