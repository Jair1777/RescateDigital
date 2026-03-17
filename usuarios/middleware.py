from django.shortcuts import redirect
from django.urls import resolve

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page other
    than login and registration.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            # Allow access to admin, login, setup or static files
            path = request.path_info
            if not (path.startswith('/usuarios/login/') or 
                    path.startswith('/usuarios/registro/') or 
                    path.startswith('/admin/') or 
                    path.startswith('/static/') or 
                    path.startswith('/media/')):
                return redirect('login')
        return self.get_response(request)
