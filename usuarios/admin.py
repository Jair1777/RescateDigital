from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'puntos_acumulados', 'ranking', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Gamificación', {'fields': ('puntos_acumulados', 'ranking')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Gamificación', {'fields': ('puntos_acumulados', 'ranking')}),
    )

admin.site.register(Usuario, CustomUserAdmin)
