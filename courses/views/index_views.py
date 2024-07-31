from django.shortcuts import render, get_object_or_404
from django.views import View
from courses.forms import ContactForm
from courses.models import Course, Category, Comment
from teachers.models import Teacher
from django.core.mail import send_mail
from django.conf import settings


class IndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        category_id = request.GET.get('category_id')
        comments = Comment.objects.filter(is_published=True)
        teachers = Teacher.objects.all()
        courses = Course.objects.all().order_by('title')

        if category_id:
            category = get_object_or_404(Category, id=category_id)
            courses = Course.objects.filter(category=category).order_by('title')
        else:
            courses = Course.objects.all().order_by('title')

        context = {'categories': categories,
                   'teachers': teachers,
                   'courses': courses,
                   'comments': comments,
                   'active_page': 'active'}
        return render(request, 'courses/index.html', context)


class CoursePage(View):
    def get(self, request):
        categories = Category.objects.all()
        category_id = request.GET.get('category_id')

        if category_id:
            category = get_object_or_404(Category, id=category_id)
            courses = Course.objects.filter(category=category).order_by('title')
        else:
            courses = Course.objects.all().order_by('title')

        context = {
            'categories': categories,
            'courses': courses,
            'selected_category': category if category_id else None
        }
        return render(request, 'courses/course.html', context)


class CourseDetailView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        context = {
            'course': course
        }
        return render(request, 'courses/course-detail.html', context)


class ContactPage(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'courses/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"Message from {name}: {subject}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return render(request, 'courses/contact_success.html')
        return render(request, 'courses/contact.html', {'form': form})


class AboutPage(View):
    def get(self, request):
        comments = Comment.objects.filter(is_published=True)
        context = {'comments': comments,}
        return render(request, 'courses/about.html', context)
