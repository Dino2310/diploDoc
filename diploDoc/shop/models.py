from django.db import models
from django.contrib.auth.models import User

STATUS = [
    ('open', 'open'),
    ('archived', 'archived')
]

ORDER_STATUS = [
    ('created', 'Создан'),
    ('assembling', 'В сборке'),
    ('delivering', 'В пути'),
    ('arrived', 'В пункте выдачи'),
    ('received', 'Получен'),
    ('cancelled', 'Отменен'),
    ('returned', 'Возврат'),
]


class Product(models.Model):
    """Модель описания продукта"""

    name = models.CharField(
        max_length=200, unique=True, verbose_name='Наменование продукта'
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name='URL'
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение'
    )
    description = models.CharField(
        max_length=250, blank=True, null=True, verbose_name='Описание'
    )
    price = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, verbose_name='Цена'
    )
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name="Остаток"
    )
    attributes = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name='Характеристики'
    )
    status = models.CharField(max_length=255, choices=STATUS, default='open')

    def __str__(self):
        return self.name


class Marketing(models.Model):
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение'
    )
    attributes = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name='Описание'
    )
    finished = models.DurationField(
        verbose_name='Дата завершения'
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name='URL'
    )

    # def __str__(self):
    #     return self.slug


class SubUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, verbose_name="Пользователь"
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name='URL'
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение'
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %'
    )
    attributes = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name='Описание'
    )
    url_home = models.TextField(
        max_length=255, blank=True, null=True
    )
    delivery_address = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name='Адрес доставки'
    )
    phone = models.CharField(max_length=20, null=True, default='+7(000)000-00-00')

    def __str__(self):
        return self.user.username


class Delivery_address(models.Model):
    address = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name='Адрес'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="Пользователь"
    )


class Order(models.Model):
    """Инициализация заказа"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    date = models.DateField(auto_now_add=True, verbose_name="Дата добавления"
                            )
    status = models.TextField(
        max_length=255, blank=True, null=True, choices=ORDER_STATUS, default='assembling', verbose_name='Статус заказа'
    )
    paid = models.TextField(
        default="SBP", verbose_name='Способ оплаты', blank=True, null=True
    )
    deliveryAddress = models.ForeignKey(
        Delivery_address, on_delete=models.CASCADE, verbose_name="Адрес Доставки", blank=True, null=True
    )

    def __str__(self):
        return f"Корзина {self.user.username} {self.status=} "

    def total_sum(self):
        return sum([i.price for i in self.reservproduct_set.all()])

    def get_status_style(self):
        status_object = {
            'is-light': ['created', 'assembling', 'delivering'],
            'is-success': ['arrived', 'received'],
            'is-danger': ['cancelled', 'returned', 'finish']
        }
        return [key for key in status_object.keys() if self.status in status_object[key]][0]
    


class ReservProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, verbose_name="Продукт", null=True)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Ссылка на заказ')

    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена'
                                )
    quantity = models.PositiveSmallIntegerField(
        default=1, verbose_name="Количество", blank=False
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка'
    )
    comment = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name='Примечание'
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name='URL'
    )


class Education(models.Model):
    word = models.CharField(
        max_length=200, unique=True, verbose_name='Ключевое слово'
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение'
    )
    name = models.CharField(
        max_length=200, unique=True, verbose_name='Наменование'
    )
    attributes = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name='Описание'
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name='URL'
    )


class ContetnLearn(models.Model):
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, default=None, null=True)
    text = models.TextField(blank=True, default=None, null=True)
    education = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True)
    queue = models.PositiveSmallIntegerField()


class Categorical(models.Model):
    """id, prod, RS485, Wi_Fi, TWI, buttons, sensors, panels_management, controllers_management, relay"""
    prod = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    RS485 = models.BooleanField(blank=True, default=False)
    Wi_Fi = models.BooleanField(blank=True, default=False)
    TWI = models.BooleanField(blank=True, default=False)
    buttons = models.BooleanField(blank=True, default=False)
    sensors = models.BooleanField(blank=True, default=False)
    panels_management = models.BooleanField(blank=True, default=False)
    controllers_management = models.BooleanField(blank=True, default=False)
    relay = models.BooleanField(blank=True, default=False)
