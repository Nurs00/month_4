from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


# class Category_type(BaseModel):
#     name = models.CharField(max_length=255, verbose_name="Название")
#
#     def __str__(self) -> str:
#         return f"{self.name}"
# #
#     class Meta:
#         db_table = 'category'
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Дарованное имя")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(BaseModel):
    image = models.ImageField(upload_to='products', null=True, blank=False, verbose_name="Фото")
    title = models.CharField(max_length=200)
    text = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        Category,
        verbose_name="Категория",
        related_name="products"
    )

    def __str__(self) -> str:
        return f"{self.title} {self.rate}"

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'