from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.getUsers, name='users'),
    path('register', views.register, name='register'),

    path('deleteUser/<str:pk>', views.deleteUser, name='delete'),

    path('login/', auth_views.LoginView.as_view(template_name='RoleAccess/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='RoleAccess/logout.html'), name='logout'),
]