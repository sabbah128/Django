from django.shortcuts import render, get_object_or_404
from blog.models import Blog


def list_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/list.html', {'blogs': blogs})

# pk=primary key, and it will be used to retrieve a single Blog record from the database.
def detail_blog(request, pk): 
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})
