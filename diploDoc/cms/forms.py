from django import forms

from shop.models import Product


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
