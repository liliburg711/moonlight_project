from django.contrib import admin
from .models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'slug', 'price', 'available', 'created', 'updated')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'price', 'available', 'created', 'updated')
    list_editable = ('price', 'available')
    search_fields = ('category__name', 'title', 'description', 'price')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 25

admin.site.register(Product, ProductAdmin)