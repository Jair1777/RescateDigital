from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Opcion
from usuarios.models import Usuario

def lista_juegos(request):
    quizzes = Quiz.objects.all()
    return render(request, 'gamificacion/lista_juegos.html', {'quizzes': quizzes})

def ranking(request):
    usuarios = Usuario.objects.filter(is_superuser=False).order_by('-puntos_acumulados')[:20]
    return render(request, 'gamificacion/ranking.html', {'usuarios': usuarios})

@login_required(login_url='/admin/login/?next=/')
def jugar_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    preguntas = quiz.preguntas.all()
    
    if request.method == 'POST':
        puntos_ganados = 0
        total_preguntas = preguntas.count()
        correctas = 0
        
        for pregunta in preguntas:
            opcion_id = request.POST.get(f'pregunta_{pregunta.id}')
            if opcion_id:
                opcion = get_object_or_404(Opcion, id=opcion_id)
                if opcion.es_correcta:
                    puntos_ganados += 10
                    correctas += 1
        
        # Update user points
        request.user.puntos_acumulados += puntos_ganados
        request.user.save()
        
        messages.success(request, f'¡Completaste el quiz! Respuestas correctas: {correctas}/{total_preguntas}. Ganaste {puntos_ganados} puntos.')
        return redirect('juegos_lista')
        
    return render(request, 'gamificacion/jugar_quiz.html', {'quiz': quiz, 'preguntas': preguntas})
