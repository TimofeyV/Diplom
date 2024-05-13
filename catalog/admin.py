from django.contrib import admin
from .models import *

@admin.action(description='Сбросить длительность приготовления рецептов')
def reset_durations(modeladmin, request, queryser):
    queryser.update(durations = 0)


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',  'available', 'created',
                    'updated',]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price',  'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class CatModAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CatMod, CatModAdmin)


class ModificatorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',  'available', 'created',
                    'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price',  'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Modificators, ModificatorsAdmin)