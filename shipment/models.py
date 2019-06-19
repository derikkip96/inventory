from django.db import models
from order.models import SalesOrder
from inve.models import StockMaster,Tax
# Create your models here.
class Shipment(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    trans_type = models.IntegerField()
    comments = models.TextField()
    status = models.BooleanField(default=True)
    packed_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ShipmentDetails(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    stock = models.ForeignKey(StockMaster,on_delete=models.CASCADE, to_field='stock_id')
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)