from .views import *
from . import views
from django.urls import path , include

urlpatterns = [ 
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>', views.add_cart, name='add_cart'),
    # path('delete_cart/<int:cart_id>', CartDeleteView.as_view(), name='cart_delete'),
]