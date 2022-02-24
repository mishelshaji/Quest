from django.urls import path
from .views import *

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/update/<int:id>/', category_update, name='category_update'),
    path('category/delete/<int:id>/', category_delete, name='category_delete'),

    path('brand/', BrandListView.as_view(), name='brand_list'),
    path('brand/create/', BrandCreateView.as_view(), name='brand_create'),
    path('brand/update/<id>/', BrandUpdateView.as_view(), name='brand_update'),
    path('brand/delete/<id>/', BrandDeleteView.as_view(), name='brand_delete'),

    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/update/<id>/', product_update, name='product_update'),
    path('product/delete/<id>/', product_delete, name='product_delete'),
]