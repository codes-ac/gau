from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name = "homepage"),
    path('student_login', TemplateView.as_view(template_name='student_login.html'), name = "student_login"),
    path('student_registration', TemplateView.as_view(template_name='student_registration.html'), name = "student_registration"),
]