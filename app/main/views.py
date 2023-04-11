from django.shortcuts import render, redirect
from .froms import RegistrationFrom
from django.contrib.auth import login, logout, authenticate


def index(request):
    return render(request, 'home/index.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = RegistrationFrom()

    args = {'form': form}

    return render(request, 'registration/sign_up.html', args)