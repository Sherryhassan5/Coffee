from django.contrib import admin
from django.urls import path
from coffeeapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('product/<int:id>', views.product, name='product'),
]
