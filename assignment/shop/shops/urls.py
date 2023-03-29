from django.urls import path
from .views import shop_list, shop_detail, shop_create, shop_update, search_shops

urlpatterns = [
    path('', shop_list, name='shop_list'),
    path('<int:pk>/', shop_detail, name='shop_details'),
    path('create/', shop_create, name='shop_create'),
    path('<int:pk>/update/', shop_update, name='shop_update'),
    path('search/', search_shops, name='search_form'),
    path('search/', search_shops, name='search_results'),
]
