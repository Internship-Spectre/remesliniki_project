from django.shortcuts import render
from .models import Material


def index(request):
    materials = Material.objects.all()

    args = {'materials': materials}
    return render(request, 'materials/index.html', args)