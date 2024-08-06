from django.shortcuts import render

from product.models import Category

# Create your views here.
def online_server(request):
    categories = Category.objects.all()
    
    return render(request, 'faq/online_server.html',{
        'categories':categories
    })

def questions(request):
    categories = Category.objects.all()
    
    return render(request, 'faq/questions.html',{
        'categories':categories
    })