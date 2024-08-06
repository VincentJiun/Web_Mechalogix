from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Product

# Create your views here.
def product_home(request):
    categories = Category.objects.all()
    
    return render(request, 'product/product_home.html',{
        'categories': categories,
    })

def product_view(request, slug):
    total = 0
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    if category.specification:
        specifications = list(category.specification.split(','))
    else:
        specifications = []

    products = Product.objects.filter(category=category)
    
    return render(request, 'product/product_view.html', {
        'categories': categories,
        'category': category,
        'products': products,
        'specifications': specifications,
    })

