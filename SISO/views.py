from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'SISO/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = request.POST.get('username')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct username or password.')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'SISO/register.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'SISO/signin.html')


def signout(request):
    logout(request)
    return redirect('home')
