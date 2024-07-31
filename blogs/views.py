from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from courses.forms import CommentForm
from courses.models import Comment
from blogs.models import Blog, Author, BlogImage


class BlogPage(View):
    def get(self, request):
        blogs = Blog.objects.all()
        recent_blogs = Blog.objects.order_by('-date_added')[:5]
        authors = Author.objects.all()
        return render(request, 'blogs/blog.html', {'blogs': blogs, 'recent_blogs': recent_blogs, 'authors': authors})


class SinglePage(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        recent_blogs = Blog.objects.order_by('-date_added')[:5]
        images = BlogImage.objects.filter(blog_id=blog)
        comments = blog.comments.filter(is_published=True)
        form = CommentForm()
        context = {
            'blog': blog,
            'blog_pk': pk,
            'images': images,
            'recent_blogs': recent_blogs,
            'form': form,
            'comments': comments
        }
        return render(request, 'blogs/single.html', context)

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = blog
            comment.is_published = True
            comment.save()
            return redirect('single', pk=pk)
        recent_blogs = Blog.objects.order_by('-date_added')[:5]
        images = BlogImage.objects.filter(blog_id=blog)
        comments = blog.comments.filter(is_published=True)
        context = {
            'blog': blog,
            'blog_pk': pk,
            'images': images,
            'recent_blogs': recent_blogs,
            'form': form,
            'comments': comments
        }
        return render(request, 'blogs/single.html', context)
