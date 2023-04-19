from django.shortcuts import render
from .models import Product
from materials.models import Material
# Create your views here.

def products_search(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
        query = ''

    context = {
        'products': products,
        'query': query
    }
    return render(request, 'products/index.html', context)

def product_list_by_material(request, material_name):
    material = Material.objects.get(name=material_name)
    products = Product.objects.filter(materials=material)
    context = {'products': products}
    return render(request, 'products/index.html', context)