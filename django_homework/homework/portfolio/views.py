from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Portfolio, Message
from .forms import MessageForm


# Create your views here.
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'portfolio/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'portfolio/loginuser.html', {'form': AuthenticationForm(),
                                                                'error': 'Incorrect username or password.'})
        else:
            login(request, user)
            return redirect('home')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'portfolio/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'A user with this name already exists.'})
        else:
            return render(request, 'portfolio/signupuser.html', {
                'form': UserCreationForm(),
                'error': "Passwords don't match, please try again."
            })


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def home(request):
    datas = Portfolio.objects.all()
    return render(request, 'portfolio/home.html', {'datas': datas})


def about(request):
    return render(request, 'portfolio/about.html')


def works(request):
    datas = Portfolio.objects.all()
    return render(request, 'portfolio/work.html', {'datas': datas})


def contact(request):
    if request.method == 'GET':
        return render(request, 'portfolio/contact.html', {'form': MessageForm()})
    else:
        try:
            form = MessageForm(request.POST)
            new_message = form.save(commit=False)
            new_message.user = request.user
            new_message.save()
            return redirect('home')
        except ValueError:
            return render(request, 'portfolio/contact.html', {
                'form': MessageForm(),
                'error': 'Incorrect data. Try again'
            })


def index(request):
    return render(request, 'portfolio/index.html')


def viewmessages(request):
    if request.user.username == 'admin':
        messages = Message.objects.all()
        return render(request, 'portfolio/viewmessages.html', {'messages': messages})
    else:
        return redirect('index')
