from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name = "homepage"),
    path('student_login', TemplateView.as_view(template_name='student_login.html'), name = "student_login"),
    path('student_registration', TemplateView.as_view(template_name='student_registration.html'), name = "student_registration"),
    path('register/student/', RegisterStudentView.as_view(), name='register_student'),
    path('login/student/', LoginStudentView.as_view(), name='login_student'),
    path('register/teacher/', RegisterTeacherView.as_view(), name='register_teacher'),
    path('login/teacher/', LoginTeacherView.as_view(), name='login_teacher'),
    path('student/<str:student_id>/profile/', StudentProfileView.as_view(), name='user_profile'),
]