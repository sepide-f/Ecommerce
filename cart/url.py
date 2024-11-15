from django.urls import path
from .views import add_to_cart, delete_from_cart

urlpatterns = [
    path("add-to-cart/<int:product_id>/", add_to_cart, name='add'),
    path("delete-from-cart/<int:product_id>/", delete_from_cart, name='delete_from_cart'),

]
