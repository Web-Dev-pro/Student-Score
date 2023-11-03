from django.urls import path
from .views import student_dashboard, teacher_dashboard, change_score

urlpatterns = [
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('change_score/<int:score_id>/', change_score, name='change_score'),
]