from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.template.defaulttags import register
from .forms import *
# Create your views here.

@register.filter
def range_filter(value):
    return range(value)

def home(request):
    coffee = Coffee.objects.all()
    context = {'coffee':coffee}
    return render(request, 'coffeeapp/index.html', context)


def store(request):
    coffee = Coffee.objects.all()
    context = {'coffee':coffee}
    return render(request, 'coffeeapp/store.html', context)


def product(request, id):
    product = get_object_or_404(Coffee, id = id)
    reviews = CoffeeReview.objects.filter(coffee_id=id)
    context = {'product':product, 'reviews':reviews,}
    return render(request, 'coffeeapp/product.html', context)


def check_store(request):
    stores  = None
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            coffee = form.cleaned_data['coffee']
            stores = CoffeeStore.objects.filter(coffee = coffee)
    else:
        form = CoffeeForm()
    context = {'stores':stores, 'form':form}
    return render(request, 'coffeeapp/check_store.html', context) 