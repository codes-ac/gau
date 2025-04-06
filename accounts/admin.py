from django.contrib import admin
from .models import Student, Teacher

class StudentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Student model.
    """
    list_display = ('student_id', 'name', 'phone_number','class_number', 'payment_status', 'teacher')  # Display relevant fields
    search_fields = ('name', 'student_id')  # Enable search functionality
    list_filter = ('teacher',)  # Add filter for teachers

class TeacherAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Teacher model.
    """
    list_display = ('name', 'email', 'school', 'student_count')  # Display name, email, and student count
    search_fields = ('name', 'email')  # Enable search functionality

    def student_count(self, obj):
        """
        Method to count the number of students associated with the teacher.
        """
        return obj.students.count()  # Use the related name 'students' to count

    student_count.short_description = 'Number of Students'  # Set the column header

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)