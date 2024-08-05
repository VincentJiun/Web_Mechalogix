from django.shortcuts import render

# Create your views here.
from product.models import Category

def index(request):
    categories = Category.objects.all()

    return render(request, 'home/index.html',{
        'categories': categories
    })

def contact(request):
    categories = Category.objects.all()

    return render(request, 'home/contact.html',{
       'categories': categories 
    })

def reward_points(request):
    categories = Category.objects.all()

    return render(request, 'home/reward_points.html',{
        'categories': categories
    })
