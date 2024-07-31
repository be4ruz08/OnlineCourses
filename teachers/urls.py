from django.urls import path
from teachers.views import TeacherPage, TeacherDetail

urlpatterns = [
    path('', TeacherPage.as_view(), name='teacher'),
    path('teacher/<int:teacher_id>/', TeacherDetail.as_view(), name='teacher_detail'),
]
