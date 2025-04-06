from rest_framework import serializers
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Student model.
    Used for creating and validating student data.
    """
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'password', 'father_name', 'class_number', 'roll_number',
                  'email', 'school', 'phone_number', 'gender', 'payment_status']
        read_only_fields = ['student_id', 'password', 'payment_status']

class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Teacher model.
    Used for creating and validating teacher data.
    """
    class Meta:
        model = Teacher
        fields = ['name', 'school', 'email', 'password']
