from django.shortcuts import render
from django.db.models import Q
from .models import Product

def product_list(request):
    # Get search query from URL parameters
    query = request.GET.get('q')
    
    if query:
        # Search in product names and descriptions
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )
    else:
        # Show all products if no search query
        products = Product.objects.all()
    
    return render(request, 'products/product_list.html', {
        'products': products,
        'query': query
    })