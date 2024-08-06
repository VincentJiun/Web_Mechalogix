from django.shortcuts import render

from product.models import Category
from .models import News

# Create your views here.

def company(request):
    categories = Category.objects.all()

    return render(request, 'about/company.html',{
        'categories': categories
    })

def history(request):
    categories = Category.objects.all()

    return render(request, 'about/history.html',{
        'categories': categories
    })

def team(request):
    categories = Category.objects.all()

    return render(request, 'about/team.html',{
        'categories': categories
    })

def product_advantages(request):
    categories = Category.objects.all()

    return render(request, 'about/advantages.html',{
        'categories': categories
    })

def recruitment(request):
    categories = Category.objects.all()

    return render(request, 'about/recruitment.html',{
        'categories': categories
    })

def news(request):
    categories = Category.objects.all()
    news = News.objects.all()

    return render(request, 'about/news.html',{
        'categories': categories,
        'news': news
    })