from django.urls import path
from.import views


urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('terms',views.terms,name='terms'),
    path('product_list',views.product_list,name='product_list'),
    path('about',views.about,name='about'),
    path('orders',views.orders,name='orders'),
    path('order_detail/<int:id>/',views.order_detail,name='order_detail'),
    path('faqs',views.faqs,name='faqs'),
    path('login_process',views.login_process,name="login_process"),
    path('register',views.registration,name="register"),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    path('update_item',views.updateItem,name='update_item'),
    path('processed_order',views.procesedOrder,name='processed_order'),
    path('product_detail/<int:id>/',views.product_detail, name="product_detail"),
]