from django.contrib import admin

# Register your models here.

from post.models import Product
from post.models import Category

admin.site.register(Product)

admin.site.register(Category)