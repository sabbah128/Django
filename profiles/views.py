from django.shortcuts import render, redirect, get_object_or_404
from profiles.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('blog_list')
    else:
        form = RegisterForm()
        return render(request, "profiles/register.html", {"form": form})

def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, "profiles/profile.html", {"user": user})