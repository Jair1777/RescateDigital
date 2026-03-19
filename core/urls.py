from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('historia/', views.historia, name='historia'),
    path('sobre-el-proyecto/', views.sobre_proyecto, name='sobre_proyecto'),
]
