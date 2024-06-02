from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

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
    context = {'product':product}
    return render(request, 'coffeeapp/product.html', context)