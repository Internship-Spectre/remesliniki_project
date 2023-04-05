from django.shortcuts import render
from main.models import Material


def index(request):
    return render(request, 'home/index.html')



def material(request):
    materials = Material.objects.all()
    return render(request, 'home/material.html', {'materials': materials})