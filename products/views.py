from django.http import JsonResponse
from .models import Product
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_products_by_name(request, name):
    products = Product.objects.filter(name__icontains=name)
    product_data = [
        {"id": product.id, "name": product.name, "description": product.description, "price": str(product.price)} for
        product in products]

    return JsonResponse({'products': product_data}, status=200)
