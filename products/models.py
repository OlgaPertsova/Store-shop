from django.db import models
from users.models import User


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name="товар")
    quantity = models.PositiveIntegerField(default=0, verbose_name="количество")
    create_database = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def sum(self):
        return self.quantity * self.product.price

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum())
        }
        return basket_item

    def __str__(self):
        return f"Корзина для {self.user.username} | Продукт {self.product.name}"

    class Meta:
        verbose_name = "товар в корзине"
        verbose_name_plural = "Корзина"


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категории")
    description = models.TextField(blank=True, verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категории"
        verbose_name_plural = "Категорию"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    image = models.ImageField(upload_to="products_images/", blank=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание товара")
    prod_description = models.CharField(max_length=100, blank=True, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    add_photo = models.ImageField(upload_to="products_images/add/", blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "Изображения"
