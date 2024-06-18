from django.db import models

STATUS = [
    ('open', 'open'),
    ('archived', 'archived')
]


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.FileField(default='default.png')
    status = models.CharField(max_length=255, choices=STATUS, default='open')
    category = models.ForeignKey('cms.Category', on_delete=models.CASCADE,null = True,blank=True)
    brand = models.ForeignKey('cms.Brand', on_delete=models.CASCADE,null = True,blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name

# Create your models here.
