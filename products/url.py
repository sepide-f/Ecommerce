from django.urls import path
from .views import search_products_by_name

urlpatterns = [
    path('products/search/<str:name>/', search_products_by_name, name='search_products_by_name'),
]