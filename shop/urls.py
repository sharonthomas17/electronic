from django.contrib import admin
from django.urls import path
from shop import views



urlpatterns = [
    #path('', admin.site.urls),
    path('view/',views.shop_view),
    path('shop_create/',views.shop_creat),
    path('shop_delete/<pk>',views.shop_delete),
    path('item/',views.item_view),
    path('item_create/',views.item_creat),
    path('item_delete/<pk>',views.item_delete),

    
]
    