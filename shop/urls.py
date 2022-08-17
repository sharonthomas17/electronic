from django.contrib import admin
from django.urls import path
from shop import views



urlpatterns = [
    #path('', admin.site.urls),
    path('',views.shop_view),
    path('shop_create/',views.shop_creat),
    path('shop_delete/<pk>',views.shop_delete),
    path('shop_update/<pk>',views.shop_update),
    path('view/',views.item_view),
    path('item_create/',views.item_creat),
    path('item_delete/<pk>',views.item_delete),
    path('item_update/<pk>',views.item_update),

    
]
    