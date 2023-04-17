from django.shortcuts import render, redirect
from .froms import RegistrationFrom
from django.contrib.auth import login, logout, authenticate
from materials.models import Material


def index(request):
    materials = Material.objects.all()

    args = {'materials': materials}

    return render(request, 'home/index.html', args)


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