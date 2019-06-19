from django.urls import path
from . import views
from inve.views import CreateUnit,CreateCategory,Item,TaxCreate
app_name = 'inve'

urlpatterns = [
    path('', views.showme, name='product_list'),
    path('unit/create', CreateUnit.as_view(), name='unit_create'),
    path('category/create', CreateCategory.as_view(), name='category_create'),
    path('item/create', Item.as_view(), name='item_create'),
    path('tax/create',TaxCreate.as_view(), name='tax_create')
]