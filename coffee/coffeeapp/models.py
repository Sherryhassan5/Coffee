from django.db import models
from django.utils import timezone
# Create your models here.


class Coffee(models.Model):
    choose = [
        ('CA', 'cappuccino'),
        ('LT', 'latte'),
        ('ES', 'espresso'),
        ('BL', 'black'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='coffeeapp/')
    added_at = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=choose) 
    description = models.TextField(default='')
    def __str__(self):
        return self.name
    
class CoffeeReview(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    rating = models.IntegerField()
    given_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review for {self.coffee.name}'

class CoffeeFormula(models.Model):
    coffee = models.OneToOneField(Coffee,on_delete=models.CASCADE)
    formula = models.CharField(max_length=200)


    def __str__(self):
        return f'formula for {self.coffee}'
    

class CoffeeStore(models.Model):
    coffee = models.ManyToManyField(Coffee)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name