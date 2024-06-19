
from django.urls import path
from .. import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('search/', views.search, name = 'search'),
    path('category/', views.category, name = 'category'),
    path('learn/', views.learn, name = 'learn'),
    path('prod/', views.prod, name = 'prod'),
    path('a/', views.ajax_ansvwer, name = 'a'),
    path('search/', views.search, name = 'search'),
    path('count/', views.count_prod, name='count'),
    path('about/', views.about, name='about'),

    ]
urlpatterns += [
    path('products/',views.products, name='products'),
    path('orders/',views.orders, name='orders'),
    path('ed_materials/',views.ed_materials, name='ed_materials'),
    path('customers/',views.customers, name='customers'),
    path('add_product/',views.add_product, name='add_product'),
    path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
    path('archive_product/<int:pk>',views.archive_product, name='archive_product')
]
