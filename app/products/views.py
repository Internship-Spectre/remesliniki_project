from django.shortcuts import render
from .models import Product

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
