from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


def list_blogs(request):
    blogs = Blog.objects.all().order_by('-date_published')
    return render(request, 'blog/list.html', {'blogs': blogs})

# pk=primary key, and it will be used to retrieve a single Blog record from the database.
def detail_blog(request, pk): 
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})

# class BlogCreateView(generic.CreateView):
#     model = Blog
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Blog
    fields = ['title', 'content']
    success_message = "Blog Created Successfully!"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)