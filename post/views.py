from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from post.forms import ProductCreateForm, CategoryCreateForm, CommentCreateForm
from post.models import Product, Category, Comment


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

def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        context = {
            'product': product,
            'form': CommentCreateForm()
        }
        return render(request, 'products/detail.html', context=context)
    elif request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            Comment.objects.create(**form.cleaned_data, product_id=product_id)
            return redirect(f'/product/{product_id}')
        context = {
            'form': form
        }
        return render(request, 'products/detail.html', context=context)
def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    elif request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/products/')
        context = {
            'form': form
        }
        return render(request, 'products/create.html', context=context)

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

def categories_create_view(request):
    if request.method == 'GET':
        context = {
            'form': CategoryCreateForm()
        }
        return render(request, 'category/create.html', context=context)
    elif request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/category/')
        context = {
            'form': form
        }
        return render(request, 'category/create.html', context=context)

