from django.urls import path

from blogs.views import BlogPage, SinglePage


urlpatterns = [
    path('blog/', BlogPage.as_view(), name='blog'),
    path('blog/single/<int:pk>/', SinglePage.as_view(), name='single'),

]
