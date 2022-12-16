from django.urls import path
from django.urls import include
from .views import *
from . import views

urlpatterns = [
    path('', views.entry_welcome, name='welcome'),
    path('products/', views.entry_welcome, name='products'),
    path('categories/', views.category_list, name='categories'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('product/<int:pk>/add_to_shopping/', AddProductToShopping.as_view(), name='add_to_shopping'),
    path('product/<pk>/delete/', DeleteProductFormView.as_view(), name='delete_product'),
    path('product/<pk>/update/', UpdateProductFormView.as_view(), name='update_product'),
    path('<pk>/update', UpdateView.as_view()),
    path('add_product/', AddProductFormView.as_view(), name='create'),
    path('add_category/', AddCategoryFormView.as_view(), name='createcategory'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('product/<pk>/buy/', BuyProductFormView.as_view(), name='buy_product'),
    path('product/<pk>/request/', RequestProductFormView.as_view(), name='request_product'),
    path('buy/', ListBuyProductFormView.as_view(), name='list_buy_product'),
    path('request/', ListRequestProductFormView.as_view(), name='list_request_product')

]
#urlpatterns = [
 #   path('', views.entry_welcome, name='entry_welcome'),
  #  path('', views.add_product, name='add_product'),
   # path('', views.add_number_of_products, name='add_number_of_products'),
    #path('', views.table_view, name='table_view'),
    #path('', views.remove_product, name='remove_product'),

#]