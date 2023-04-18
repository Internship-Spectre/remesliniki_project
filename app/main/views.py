from django.shortcuts import render, redirect
from .forms import RegistrationFrom
from django.contrib.auth import login
from materials.models import Material
from products.models import Product


def index(request):
    materials = Material.objects.all()[:10]
    products = Product.objects.all()[:10]


    args = {
        'materials': materials,
        'products': products
    }

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