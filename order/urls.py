from django.urls import path
from order.views import SalesTypeView
app_name = 'order'

urlpatterns = [
    path('settings/sales_type', SalesTypeView.as_view(), name='sales_type'),
]