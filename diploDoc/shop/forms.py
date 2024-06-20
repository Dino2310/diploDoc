from django import forms
from .models import *

# class CreateOrderForm(forms.ModelForm):
#     first_name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}
#     ))
#     last_name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Введите вашу фамилию'}
#     ))
#     phone_number = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'input', 'placeholder': 'Номер телефона'}
#     ))
#     requires_delivery = forms.CharField(
#         widget=forms.RadioSelect(),
#         choices=[
#             ('0', False),
#             ('1', True),
#         ],
#         initial=0
#     )
#     delivery_address = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'delivery_address',
#                 'rows': 2,
#                 'placeholder': 'Введите адрес доставки'
#             }
#         ),
#         required=False
#     ) 
#     payment_on_get = forms.CharField(
#         widget=forms.RadioSelect(),
#         choices=[
#             ('0', False),
#             ('1', True),
#         ],
#         initial='card'
#     )


#     class Meta:
#         model = Order
#         fields = ["title", "content", "slug"]


# class EducationForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'input', 'placeholder': 'Название поста'}
#     ))
#     word = forms.CharField(widget=forms.Textarea(
#         attrs={'class': 'input', 'placeholder': 'Ключевое слово'}
#     ))
#     slug = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'input', 'placeholder': 'Идентификатор поста'}
#     ))
#     slug = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'input', 'placeholder': 'Идентификатор поста'}
#     ))
    
#     class Meta:
#         model = Education
#         fields = ["title", "content", "slug"]

class ProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.TextInput(
        attrs={"type": "image"}
    ))
    price = forms.DecimalField(
        max_digits=10, decimal_places=2
    )

    
    class Meta:
        model = Product
        fields = ["name", "slug", "image", "description", "price", "quantity", "attributes"]

class MarketingForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.TextInput(
        attrs={"type": "image"}
    ))
    slug = forms.SlugField(widget=forms.TextInput(
        attrs={"type": "slug"}
    ))
    
    class Meta:
        model = Marketing
        fields = ["image", "attributes", "finished", "slug"]

class SubUserForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.TextInput(
        attrs={"type": "image"}
    ))
    slug = forms.SlugField(widget=forms.TextInput(
        attrs={"type": "slug"}
    ))
    url_home = forms.URLField(widget=forms.TextInput(
        attrs={"type": "url_home"}
    ))
    
    class Meta:
        model = SubUser
        fields = ["user", "slug", "image", "discount", "url_home", "attributes", "delivery_address"]
        
        
class Delivery_addressForm(forms.ModelForm):
     
    class Meta:
        model = Delivery_address
        fields = ["address", "user"]
        
# class CreateOrderForm(forms.ModelForm):
#     date = forms.DateField(widget=forms.DateInput(
#         attrs={"type": "date"}
#     ))
#
#     class Meta:
#         model = Order
#         fields = ["user", "price", "quantity", "date", "status", "paid", "delivery_address"]
        
class ProductsForm(forms.ModelForm):
    slug = forms.SlugField(widget=forms.TextInput(
        attrs={"type": "slug"}
    ))
    
    class Meta:
        model = ReservProduct
        fields = ["order", "product", "price", "quantity", "discount", "comment", "slug"]


class EducationForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.TextInput(
        attrs={"type": "image"}
    ))
    slug = forms.SlugField(widget=forms.TextInput(
        attrs={"type": "slug"}
    ))
    
    class Meta:
        model = Education
        fields = ["word", "attributes", "image", "name", "slug"]
class ProductForm(forms.ModelForm):
    title = (forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Название товара'}
    )))
    description = (forms.CharField(widget=forms.Textarea(
        attrs={'class': 'textarea', 'placeholder': 'Описание товара'}
    )))
    quantity = (forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'input', 'placeholder': 'Кол-во товара'}
    )))
    price = (forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'input', 'placeholder': 'Цена  товара'}
    )))
    image = forms.FileField(required=False)


    class Meta:
        model = Product
        fields =['title','description','quantity','price','image']
