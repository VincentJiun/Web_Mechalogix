from django.shortcuts import render

from product.models import Category

# Create your views here.

def order_cost(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/order_cost.html',{
        'categories': categories
    })

def real_time(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/real_time.html',{
        'categories': categories
    })

def utilization(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/utilization.html',{
        'categories': categories
    })

def shift_status(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/shift_status.html',{
        'categories': categories
    })

def workshop(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/workshop.html',{
        'categories': categories
    })

def sawblade(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/sawblade.html',{
        'categories': categories
    })

def real_time_app(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/real_time_app.html',{
        'categories': categories
    })

def allowable_values(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/allowable_values.html',{
        'categories': categories
    })

def automatic_reports(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/automatic_reports.html',{
        'categories': categories
    })

def sawlogix(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/sawlogix.html',{
        'categories': categories
    })

def more_solution(request):
    categories = Category.objects.all()
    
    return render(request, 'solution/more_solution.html',{
        'categories': categories
    })