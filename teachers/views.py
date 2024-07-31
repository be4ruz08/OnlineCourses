from django.shortcuts import render, get_object_or_404
from django.views import View
from teachers.models import Teacher


class TeacherPage(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, 'teachers/teacher.html', {'teachers': teachers})


class TeacherDetail(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        print(f"Teacher found: {teacher.full_name}")
        return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})
