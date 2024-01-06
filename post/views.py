from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings
from post.forms import ProductCreateForm, CategoryCreateForm, CommentCreateForm,PostForm2
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

        search = request.GET.get('search')
        print(search)

        if search:
            products = products.filter(title__contains=search)

        max_page = products.__len__() / settings.OBJECT_PER_PAGE

        if round(max_page) < max_page:
            max_page += 1
        else:
            max_page = round(max_page)

        page = request.GET.get('page', 1)

        start = (int(page) - 1) * settings.OBJECT_PER_PAGE
        end = int(page) * settings.OBJECT_PER_PAGE

        context = {
            'products': products[start:end],
            'max_page': range(1, int(max_page) + 1),
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


def product_update_view(request, product_id):
    try:
        post = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    if request.method == 'GET':
        context = {
            'form': PostForm2(instance=post),
            'post': post,
        }
        return render(request, 'products/update.html', context=context)

    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            context = {
                'form': form,
                'post': post,
            }
            return render(request, 'products/update.html', context=context)
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

