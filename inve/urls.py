from django.urls import path
from . import views
from inve.views import (CreateUnit,
                        CreateCategory,
                        Item,
                        TaxUpdateView,
                        FinanceView,LocationView,SalesPriceView
                        )

app_name = 'inve'

urlpatterns = [
    path('', views.showme, name='product_list'),
    path('settings/unit', CreateUnit.as_view(), name='unit'),
    path('category/list', CreateCategory.as_view(), name='list'),
    path('item/create', Item.as_view(), name='item_create'),
    path('tax/create',TaxUpdateView.as_view(),name='tax_edit'),
    path('settings/finance',FinanceView.as_view(),name='setting_finace'),
    path('settings/location',LocationView.as_view(),name = 'location'),
    path('sales/create',SalesPriceView.as_view(), name ='sales_price')
]