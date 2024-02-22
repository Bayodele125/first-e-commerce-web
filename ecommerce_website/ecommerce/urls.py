from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_list', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase_quantity/<int:order_id>', views.increase_quantity, name='increase_quantity' ),
    path('decrease_quantity/<int:order_id>', views.decrease_quantity, name='decrease_quantity' ),
    path('delete_order/<int:order_id>', views.delete_order, name='delete_order' ),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
]