from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer
from django.shortcuts import get_object_or_404
from .decorators import csrf_exempt_cbv
from rest_framework.generics import ListAPIView

@csrf_exempt_cbv
class ProductView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    def get_queryset(self):
        products = Product.objects.all()
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        param = self.request.query_params.get('param', None)
        if param:
            products = products.filter(name__icontains=param)
        if min_price:
            products = products.filter(price__gte=float(min_price))
        if max_price:
            products = products.filter(price__lte=float(max_price))
        return products
    
@csrf_exempt_cbv
class ProductViewById(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product)
        if not product:
            return Response({"message": "Product with id {} not found".format(id)}, status=404)
        return Response(serializer.data)
    
@csrf_exempt_cbv
class ProductCreateView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@csrf_exempt_cbv
class ProductUpdateView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def put(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

@csrf_exempt_cbv
class ProductDeleteView(APIView):
    permission_classes = [AllowAny]
    
    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=204)






