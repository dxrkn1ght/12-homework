from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('create/', views.product_create, name='create'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]