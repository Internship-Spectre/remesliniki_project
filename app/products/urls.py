from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_search, name='products_index'),
    path('products/<str:material_name>/', views.product_list_by_material, name='products_list_by_material'),
]