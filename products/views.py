from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product
from django.db.models import Q
from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def search_products(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return JsonResponse({'results': list(results.values('id', 'name', 'price'))})