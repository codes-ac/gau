from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    # < ----------- Templates Render ----------- >
    path('', TemplateView.as_view(template_name='home.html'), name = "homepage"),
    path('student_login', TemplateView.as_view(template_name='student_login.html'), name = "student-login"),
    path('student_registration', TemplateView.as_view(template_name='student_registration.html'), name = "student-registration"),
    path('student/<str:student_id>/profile/', StudentProfileView.as_view(), name='user_profile'),

    #< --------- Login and Register API ---------- >
    path('register/student/', RegisterListStudentView.as_view(), name='register-student'),
    path('login/student/', LoginStudentView.as_view(), name='login-student'),
    path('register/teacher/', RegisterTeacherView.as_view(), name='register-teacher'),
    path('login/teacher/', LoginTeacherView.as_view(), name='login-teacher'),
    path('students/', RegisterListStudentView.as_view(), name='student-get-list'),
    path('student/<str:student_id>/', StudentDetailView.as_view(), name='student-get-detail'),
]