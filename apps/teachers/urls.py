from django.urls import path
from .views import TeacherAssignment

urlpatterns = [
    path('assignments/', TeacherAssignment.as_view(), name='teachers-assignments')
]
