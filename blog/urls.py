"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog import settings
from user.views import register_view, login_view, logout_view, profile_view
from post.views import (hello_view, current_date_view, goodby_view,
                        anime_view, main_view, product_list_view,
                        one_piece_view, categories_view, product_detail_view,
                        product_create_view, categories_create_view, product_update_view)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('current_date/', current_date_view),
    path('goodby/', goodby_view),
    path('anime/', anime_view),
    path('', main_view),
    path('products/', product_list_view),
    path('product/<int:product_id>/', product_detail_view),
    path('product/<int:product_id>/update/', product_update_view),
    path('one_piece/', one_piece_view),
    path('category/', categories_view),
    path('category/create/', categories_create_view),
    path('products/create/', product_create_view),
    path('auth/register/', register_view),
    path('auth/login/', login_view),
    path('auth/logout/', logout_view),
    path('auth/profile/', profile_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
