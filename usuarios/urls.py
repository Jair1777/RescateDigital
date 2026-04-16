from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('configuracion/', views.perfil_config, name='perfil_config'),
]
