from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
# class Image(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, blank=True)
#     url = models.URLField()
#     image = models.ImageField(upload_to='images/%Y/%m/%d')
#     description = models.TextField(blank=True)
#     created = models.DateField(auto_now_add=True, db_index=True)
    
#     def __str__(self):
#         return self.title
    
# class Comment(models.Model):
#     body = models.TextField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     likes = models.ManyToManyField(User, related_name='comment_likes')
#     dislikes = models.ManyToManyField(User, related_name='comment_dislikes')
#     parent = models.ForeignKey(
#         'self', null=True, blank=True, on_delete=models.CASCADE, related_name='reply'
#     )
#     first_comment = models.ForeignKey(
#         'self', null=True, blank=True, on_delete=models.CASCADE, related_name='main_comment'
#     )

#     def __str__(self):
#         return self.body

CATEGORIES = [
    ("making an order", "Оформление заказа"),
    ("payment", "Оплата заказа"),
    ("order processing", "Обработка заказа"),
    ("order assembly", "Сборка заказа"),
    ("sending an order", "Отправка заказа"),
    ("receiving an order", "Получение заказа"),
    ("done!", "Выполнено!")
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
   
    def __str__(self):
        return self.slug
   
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

    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name="Количество")
    date = models.DateField(auto_now_add=True, verbose_name="Дата добавления"
                            )
    status = models.TextField(
        max_length=255, blank=True, null=True, choices=CATEGORIES, default=CATEGORIES[-1][0], verbose_name='Статус заказа'
        )
    paid = models.BooleanField(
        default=False, verbose_name='Способ оплаты'
        )
    delivery_address = models.ForeignKey(
        Delivery_address, on_delete=models.CASCADE, verbose_name="Пользователь"
        )
   
    def __str__(self):
        return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"
   


class Products(models.Model):


    orders = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="Пользователь"
        )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена'
                                )
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name="Количество"
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
   
    def __str__(self):
        return self.slug



class Education(models.Model):
    word = models.CharField(
        max_length=200, unique=True, verbose_name='Ключевое слово'
        )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение'
        )
    name = models.CharField(
        max_length=200, unique=True, verbose_name='Наменование продукта'
        )
    attributes = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name='Описание'
        )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name='URL'
        )
   
    def __str__(self):
        return self.slug
    

