from django.db import models
from order.models import Debtor

# Create your models here.
class CustBranch(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    billing_street = models.CharField(max_length=200)
    billing_city = models.CharField(max_length=200)
    billing_state = models.CharField(max_length=200)
    billing_zip_code = models.CharField(max_length=200)
    billing_country = models.CharField(max_length=200)
    shipping_street = models.CharField(max_length=200)
    shipping_city = models.CharField(max_length=200)
    shipping_zip_code = models.CharField(max_length=200)
    shipping_country = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
class Country(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
