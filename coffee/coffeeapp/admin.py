from django.contrib import admin
from .models import *
# Register your models here.

class CoffeeReviewAdmin(admin.TabularInline):
    model = CoffeeReview
    extra = 2


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type' , 'added_at')
    inlines = [CoffeeReviewAdmin]

class CoffeeFormulaAdmin(admin.ModelAdmin):
    list_display = ('coffee' , 'formula')

class CoffeeStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('coffee',)


admin.site.register(Coffee,CoffeeAdmin)
admin.site.register(CoffeeReview)
admin.site.register(CoffeeFormula,CoffeeFormulaAdmin)
admin.site.register(CoffeeStore,CoffeeStoreAdmin)