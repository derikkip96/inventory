from django.db import models
from django.conf import settings
from order.models import Debtor
# Create your models here.
class Payment(models.Model):
    payment_type = models.IntegerField()
    order_reference = models.CharField(max_length=50)
    invoice_reference = models.CharField(max_length=50)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    customer = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)

class PaymentTerm(models.Model):
    name = models.CharField(max_length=100)
    defaults = models.IntegerField()

class InvoicePaymentTerms(models.Model):
    terms = models.CharField(max_length=50)
    days_before_due = models.IntegerField()
    defaults = models.BooleanField(default=True)