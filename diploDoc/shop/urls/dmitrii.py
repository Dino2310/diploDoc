
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
