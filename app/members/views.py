from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm


def login_view(request):
    if request.user.is_authenticated is True:
        return redirect('books:book-list')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('books:book-list')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'members/login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books:book-list')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('members:login')
