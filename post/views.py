from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from post.models import Product, Category
def hello_view(request):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project😍')

def current_date_view(request):
    print(request)
    current_date = timezone.now().date()
    return HttpResponse(f"Time in Bishkek:{current_date}⌛")

def goodby_view(request):
    print(request)
    return HttpResponse('Goodby user! bye bye😊')

def anime_view(request):
    print(request)
    return render(request, 'anime/index.html')

def main_view(request):
    if request.method == 'GET':
        return render(request, 'Products.html')

def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products,
        }
        return render(request, 'products/list.html', context=context)


def one_piece_view(request):
    if request.method == 'GET':
        return render(request, 'anime/anime.html')

def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        print(categories)

        context = {
            'categories': categories,
        }

        return render(request, 'category/categories.html', context=context)


