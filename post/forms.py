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
