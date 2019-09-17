from django.urls import path
from order.views import SalesTypeView,SalesPriceView
app_name = 'order'

urlpatterns = [
    path('settings/sales_type', SalesTypeView.as_view(), name='sales_type'),
    path('sales/create',SalesPriceView.as_view(), name ='sales_price')
]