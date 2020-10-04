from django.db import models
from datetime import datetime

# Create your models here.
class Florist(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    photo = models.ImageField(upload_to='florist/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=250)
    ig = models.URLField(max_length=200)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return self.name