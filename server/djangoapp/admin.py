from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

class CarModelInline(admin.StackedInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    llist_display = ('model_name', 'car_type')
    list_filter = ['car_type']
    search_fields = ['model_name']

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('make_name', 'country')
    list_filter = ['country']
    search_fields = ['make_name', 'country']

# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake)