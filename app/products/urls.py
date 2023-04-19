from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_search, name='products_index'),
    
]