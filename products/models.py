from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='products')
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='products/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta: 
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', args=[self.id])
