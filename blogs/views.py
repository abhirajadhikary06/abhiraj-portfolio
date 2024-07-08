# views.py
from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'all_blogs.html', {'blogs': blogs})

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})
