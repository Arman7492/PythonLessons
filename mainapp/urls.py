from django.urls import path

from .views import about, contacts, index, product, products

urlpatterns = [
    path('about/', about),
    path('contacts/', contacts),
    path('', index),
    path('product', product),
    path('products/', products),

]
