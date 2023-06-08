from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    description = models.TextField(verbose_name='Описание')
    product_image = models.ImageField(verbose_name='Изображение товара', upload_to='images/', default='images/default_prod.jpg', blank=True)
    manufacturer = models.CharField(verbose_name='Производитель', max_length=200)
    price = models.DecimalField(verbose_name='Цена', max_digits=15, decimal_places=2)
    release_date = models.DateField(verbose_name='Дата выпуска')
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class Game(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Player(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    description = models.TextField(verbose_name='Описание игрока')
    player_image = models.ImageField(verbose_name='Фото игрока', upload_to='images/', default='images/default_user.png', blank=True)
    devices = models.ManyToManyField(Product)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    price = models.DecimalField(verbose_name='Общая цена заказа', max_digits=15, decimal_places=2)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    products = models.ManyToManyField(Product)
    price = models.DecimalField(verbose_name='Общая цена заказа', max_digits=15, decimal_places=2)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(verbose_name='Дата заказа', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'