from django.urls import path
from apps.teachers.views import AssignmentsView

urlpatterns = [
  path('assignments/', AssignmentsView.as_view(), name='teachers-assignments')
]