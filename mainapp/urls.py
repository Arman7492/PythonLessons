from django.urls import path

from .views import about, contacts, index, product, products

app_name = 'main'

urlpatterns = [
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('', index, name='index'),
    path('product', product, name='product'),
    path('products/', products, name='products'),
]
