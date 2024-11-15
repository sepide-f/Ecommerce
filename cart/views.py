from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, Product, Cart
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return Response({
        "message": "Product added to cart successfully",
        "cart_item": {
            "product_id": product.id,
            "name": product.name,
            "quantity": cart_item.quantity,
            "total_price": str(cart_item.total_price()),
        }
    }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()

    if cart_item:
        cart_item.delete()
        return JsonResponse({'message': 'Product removed from cart successfully'}, status=200)

    else:
        return JsonResponse({'message': 'Product not found in your cart'}, status=404)
