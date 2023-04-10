from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'orders/index.html')

def create_order(request):
    return render(request, 'orders/create.html')

