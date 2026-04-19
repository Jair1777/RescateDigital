from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('proyecto/', views.proyecto, name='proyecto'),
    path('historia/', views.historia, name='historia'),
    path('migrar-db/', views.run_migrations, name='run_migrations'),
    path('mapa/', views.mapa_musical, name='mapa_musical'),
    path('notificaciones/marcar-leidas/', views.marcar_notificaciones_leidas, name='marcar_notificaciones_leidas'),
]
