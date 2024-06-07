
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search/', views.search, name = 'search'),
    path('category/', views.category, name = 'category'),
    path('learn/', views.learn, name = 'learn'),
    path('prod/<int:c_id>', views.prod, name = 'prod'),

    ]
