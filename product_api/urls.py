from django.contrib import admin
from django.urls import path
from .views import ProductView, ProductViewById, ProductCreateView, ProductUpdateView, ProductDeleteView
urlpatterns = [
    path('viewproducts/', ProductView.as_view(), name='product-list'),
    path('viewproduct/<int:id>/', ProductViewById.as_view(), name='product-detail'),
    path('createproduct/', ProductCreateView.as_view(), name='product-create'),
    path('updateproduct/<int:id>/', ProductUpdateView.as_view(), name='product-update'),
    path('deleteproduct/<int:id>/', ProductDeleteView.as_view(), name='product-delete'),
]
