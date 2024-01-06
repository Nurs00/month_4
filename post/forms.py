from django import forms

from post.models import Product, Comment, Category


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'text', 'image', 'rate')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PostForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'text', 'image', 'rate')
        labels = {
            'title': 'Название продукта',
            'text': 'Текст продукта',
            'image': 'Картинка',
            'rate': 'Рейтинг',
        }
        help_texts = {
            'title': 'Введите название продукта',
            'text': 'Введите текст продукта',
            'image': 'Загрузите картинку',
            'rate': 'Введите рейтинг',
        }