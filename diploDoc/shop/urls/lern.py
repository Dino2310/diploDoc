from django.urls import path
from .. import views


urlpatterns = [
    path('savelern/', views.savelern, name = 'savelern'),]