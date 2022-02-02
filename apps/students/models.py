from django.db import models

from apps.internal.models import User
from apps.teachers.models import Teacher

GRADE_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D')
)

ASSIGNMENT_STATE_CHOICES = (
    ('DRAFT', 'DRAFT'),
    ('SUBMITTED', 'SUBMITTED'),
    ('GRADED', 'GRADED')
)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='Reference to User model')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    class Meta:
        db_table = 'students'


class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text='Reference to Student model')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, help_text='Reference to Teacher model', null=True)
    content = models.TextField(help_text='Content of the assignment', null=False)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, help_text='Grade of the assignment', null=True)
    state = models.CharField(max_length=9, choices=ASSIGNMENT_STATE_CHOICES, default='DRAFT',
                             help_text='State of the assignment', null=False)
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at')

    class Meta:
        db_table = 'assignments'
