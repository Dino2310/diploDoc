
from django.urls import path
from .. import views

urlpatterns = [
        path('detail/<str:slug>', views.detail, name='detail')

    ]