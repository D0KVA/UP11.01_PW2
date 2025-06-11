from django.db import models
from django.utils import timezone

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя коллекции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Brand(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название бренда')
    country = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Страна происхождения')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя поставщика')
    contact_info = models.TextField(null=True, blank=True, verbose_name='Контактная информация')
    photo = models.ImageField(upload_to='image/suppliers/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Items(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя позиции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, verbose_name='Коллекция', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Бренд')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')

    def __str__(self):
        return f"{self.name} - ({self.price} рублей)"
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Customer(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя')
    last_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата заказа')

    def __str__(self):
        return f"Заказ №{self.id} от {self.customer}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    item = models.ForeignKey(Items, on_delete=models.PROTECT, verbose_name='Предмет')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
