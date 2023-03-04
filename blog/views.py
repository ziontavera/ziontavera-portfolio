from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Blog


def all_blogs(request):
    print(User.objects.filter(is_superuser=True).values_list('password'))
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})