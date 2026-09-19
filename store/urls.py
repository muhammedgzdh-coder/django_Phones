from django.urls import path
from store.views.Home_Products import home , products , brands 
from store.views.basket import Cart , CartView
from store.views.Product_Details import product_detail , Search_Phones 



app_name = 'store'


urlpatterns = [

    path('', home, name='home'),

    path('products/',products,name='products'),

    path('products/<str:tag_name>/',products,name='p'),

    path('d/<int:id>/',product_detail,name='product_detail'),

    path('brands/',brands,name='brands'),

    path('search/',Search_Phones,name='search'),
    
    path('cart/add/<int:id>/',Cart,name='cart_add'),

    path('cart/',CartView,name='cart'),

   
]