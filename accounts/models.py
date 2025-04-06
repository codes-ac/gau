from django.db import models
import random
import string

class Teacher(models.Model):
    """
    Model representing a teacher.
    """
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    """
    Model representing a student.
    Each student has a unique student_id and a randomly generated password.
    """

    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]

    student_id = models.CharField(max_length=8, unique=True)
    password = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    class_number = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    school = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=6, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    teacher = models.ForeignKey(Teacher, related_name='students', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate student_id and password.
        """
        if not self.student_id:
            self.student_id = self.generate_student_id()
        if not self.password:
            self.password = self.generate_random_password()
        super().save(*args, **kwargs)

    def generate_student_id(self):
        """
        Generate a sequential student_id starting from 20250001.
        """
        last_student = Student.objects.order_by('id').last()
        if last_student:
            last_id = int(last_student.student_id)
            new_id = last_id + 1
        else:
            new_id = 20250001
        return str(new_id)

    def generate_random_password(self):
        """
        Generate a random 8-character password consisting of letters and digits.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def __str__(self):
        return self.name