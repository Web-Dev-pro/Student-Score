from django.shortcuts import render, get_object_or_404
from .models import Student, Score, Assessment, Teacher

def student_dashboard(request):
    student = get_object_or_404(Student, user=request.user)
    scores = Score.objects.filter(student=student)
    return render(request, 'student_dashboard.html', {'scores': scores})

def teacher_dashboard(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    assessments = Assessment.objects.all()
    return render(request, 'teacher_dashboard.html', {'assessments': assessments})

def change_score(request, score_id):
    score = get_object_or_404(Score, id=score_id)
    if request.method == 'POST':
        new_score = int(request.POST['new_score'])
        score.score = new_score
        score.save()
    return render(request, 'change_score.html', {'score': score})
