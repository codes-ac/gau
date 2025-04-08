import openpyxl
from django_q.tasks import schedule
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404

from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer

class RegisterListStudentView(generics.ListCreateAPIView):
    """
    API view for registering a new student.
    Automatically generates student_id and password.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single student's details by ID.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_id'

class LoginStudentView(APIView):
    """
    API view for logging in a student.
    Validates student_id and password.
    """
    def post(self, request):
        student_id = request.data.get('student_id')
        password = request.data.get('password')
        try:
            student = Student.objects.get(student_id=student_id, password=password)
            return Response({"message": "Login successful", "student_id": student.student_id}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class RegisterTeacherView(generics.CreateAPIView):
    """
    API view for registering a new teacher.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class LoginTeacherView(APIView):
    """
    API view for logging in a teacher.
    Validates email and password.
    """
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            teacher = Teacher.objects.get(email=email, password=password)
            return Response({"message": "Login successful", "email": teacher.email}, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class StudentProfileView(View):
    """
    View to display the profile of a student based on the student ID.
    """

    def get(self, request, student_id):
        student = get_object_or_404(Student, student_id=student_id)
        return render(request, 'student_profile.html', {'user': student})