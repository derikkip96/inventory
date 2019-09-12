from django.db import models
from django.conf import settings
from inve.models import StockMaster,Location
from customer.models import Supplier

# Create your models here.

from inve.models import Tax, Item
# Create your models here.
class SalesType(models.Model):
    CHOICES = (
        (False, 'No'),
        (True, 'Yes')
    )
    types = models.CharField(max_length=100)
    tax = models.BooleanField(choices=CHOICES, default=False)
    default = models.BooleanField(choices=CHOICES)

    def __str__(self):
        return self.types

class Debtor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    sales_type = models.ForeignKey(SalesType, on_delete=models.CASCADE)
    inactive = models.BooleanField(default=True)
    vat_no = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    payment_type = models.IntegerField()
    order_reference = models.CharField(max_length=50)
    invoice_reference = models.CharField(max_length=50)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='payments',)
    customer = models.ForeignKey(Debtor, on_delete=models.CASCADE, related_name='payments',)
    reference = models.CharField(max_length=50)

class PaymentTerm(models.Model):
    name = models.CharField(max_length=100)
    defaults = models.IntegerField()

class InvoicePaymentTerms(models.Model):
    terms = models.CharField(max_length=50)
    days_before_due = models.IntegerField()
    defaults = models.BooleanField(default=True)



class PurchasesOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    qty_invoked = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    act_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_type = models.ForeignKey(Tax, on_delete=models.CASCADE)
    std_cost_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_ordered = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_received = models.DecimalField(max_digits=10, decimal_places=2)
    qty_received = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class PurchasesOrderDetail(models.Model):
    CHOICES = (
        (False, 'No'),
        (True, 'Yes')
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    comments = models.TextField(max_length=200)
    order_date = models.DateTimeField()
    reference = models.CharField(max_length=30)
    requistion_no = models.CharField(max_length=50, blank=True, null=True)
    into_stock_loc = models.CharField(max_length=50)
    delivery_address = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tax_included= models.CharField(max_length=20, choices=CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class PurchasePrice(models.Model):
    stock_id = models.ForeignKey(StockMaster,on_delete=models.CASCADE, to_field='stock_id')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=50)
    conversion_factor = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    supplier_description = models.CharField(max_length=50)

class SalesOrder(models.Model):
    trans_type = models.CharField(max_length=50)
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE, related_name = 'salesorders')
    branch = models.IntegerField()
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'salesorders' )
    version = models.SmallIntegerField()
    reference = models.CharField(max_length=50)
    customer_ref = models.CharField(max_length=50, blank=True, null=True)
    order_reference_id = models.IntegerField()
    order_reference = models.CharField(max_length=200, null=True)
    comments = models.TextField(max_length=250, blank=True, null=True)
    order_date = models.DateTimeField()
    order_type = models.IntegerField()
    delivery_address = models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50, null=True)
    email = models.EmailField()
    deliver_to = models.CharField(max_length=50, blank=True, null=True)
    from_stk_loc = models.CharField(max_length=50, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_term = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SalesPrice(models.Model):
    stock = models.ForeignKey(StockMaster, on_delete=models.CASCADE, to_field='stock_id')
    sales_type = models.ForeignKey(SalesType, on_delete=models.CASCADE)
    curr_abrev = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class SalesOrderDetail(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    trans_type = models.CharField(max_length=50)
    stock_id = models.ForeignKey(StockMaster, on_delete=models.CASCADE,to_field='stock_id')
    tax_types = models.IntegerField(null=True)
    decription = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    qty_sent = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    shipment_qty = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ReceiveOrder(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    receive_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

class ReceiveOrderDetails(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=True)
    receive = models.ForeignKey(ReceiveOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    reference = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class StockMove(models.Model):
    stock = models.ForeignKey(StockMaster, on_delete=models.CASCADE, to_field='stock_id')
    order = models.CharField(max_length=50, default=0)
    receiver = models.ForeignKey(ReceiveOrder, on_delete=models.CASCADE, null=True)
    trans_type = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    trans_date = models.DateTimeField()
    person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)
    transaction_reference_id = models.IntegerField()
    transfer_id = models.IntegerField()
    order_reference = models.CharField(max_length=50)
    note = models.TextField(max_length=255)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)









