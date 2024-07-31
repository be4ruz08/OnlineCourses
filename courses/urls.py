from django.urls import path

from courses.views.index_views import IndexPage, CoursePage, CourseDetailView, ContactPage, AboutPage
from courses.views.authentication import RegisterView, LoginView, LogoutView


urlpatterns = [
    # index
    path('home/', IndexPage.as_view(), name='index'),
    path('', CoursePage.as_view(), name='course'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutPage.as_view(), name='about'),

    # auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
