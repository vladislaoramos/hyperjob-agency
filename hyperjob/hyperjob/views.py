from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from resume.models import Resume
from vacancy.models import Vacancy
from .forms import DescriptionForm


def menu(request):
    return render(request, 'menu.html')


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is None:
                return redirect('/signup/')
            else:
                login(request, user)
                return redirect('/')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'signup.html', {'form': UserCreationForm()})


def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            action = "/vacancy/new"
            entries = Vacancy.objects.all().filter(author=request.user)
        else:
            action = "/resume/new"
            entries = Resume.objects.all().filter(author=request.user)
        return render(request, 'home.html', {
            'action': action, 'form': DescriptionForm(data=request.POST), 'entries': entries})
    return render(request, 'home.html', {'action': ''})
