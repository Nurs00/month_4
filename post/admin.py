from django.contrib import admin

# Register your models here.

from post.models import Product
from post.models import Category,Comment

admin.site.register(Product)

admin.site.register(Category)
admin.site.register(Comment)