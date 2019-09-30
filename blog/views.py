from django.shortcuts import render, get_object_or_404
from blog.models import Blog


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def details(request,Blog_id):
    details = get_object_or_404(Blog, pk=Blog_id)
    return render(request, 'blog/detail.html', {'details': details})