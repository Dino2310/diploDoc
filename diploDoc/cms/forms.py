from django import forms

from shop.models import Product,ORDER_STATUS,Order


class ProductForm(forms.ModelForm):
    name = (forms.CharField(widget=forms.TextInput(
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
        fields =['name','description','quantity','price','image']

class StatusForm(forms.ModelForm):
    status = forms.ChoiceField(choices=ORDER_STATUS)
    class Meta:
        model = Order
        fields=['status']
