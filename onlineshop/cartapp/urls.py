from django.urls import path
from cartapp import views
app_name = 'cartapp'


urlpatterns = [
    path('',views.cart_detail,name= 'cart_detail'),
    path('add/<int:product_id>',views.add_cart, name= 'add_cart'),
    path('remove/<int:product_id>', views.minus, name='minus'),
    path('full_remove/<int:product_id>', views.full_remove, name='full_remove'),
]
