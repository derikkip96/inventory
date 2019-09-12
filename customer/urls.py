from django.urls import path
from customer.views import SupplierView

urlpatterns = [
    path('supplier/create', SupplierView.as_view(), name='unit_create'),
]