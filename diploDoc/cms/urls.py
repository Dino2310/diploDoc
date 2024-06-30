from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.products, name='products'),
    path('orders/',views.orders, name='orders'),
    path('status_edit/<int:pk>',views.status_edit,name='status_edit'),
    path('ed_materials/',views.ed_materials, name='ed_materials'),
    path('add_education_material/',views.add_education_material,name ='add_education_material'),
    path('customers/',views.customers, name='customers'),
    path('add_product/',views.add_product, name='add_product'),
    path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
    path('archive_product/<int:pk>',views.archive_product, name='archive_product')
]
