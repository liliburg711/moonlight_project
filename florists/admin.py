from django.contrib import admin
from .models import Florist
# Register your models here.

class FloristAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'ig', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Florist, FloristAdmin)