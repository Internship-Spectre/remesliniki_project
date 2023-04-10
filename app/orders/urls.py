from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='orders_index'),
    path('create', views.create_order, name='orders_create'),
]