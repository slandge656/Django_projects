from django.contrib import admin
from .models import*
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=['name','description','image','category_name']