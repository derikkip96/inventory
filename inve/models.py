from django.conf import settings
from django.db import models
# from order.models import ReceiveOrder
# # Create your models here.

class ItemUnit(models.Model):
    name = models.CharField(max_length=20)
    abbr =  models.CharField(max_length=20)
    inactive = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

class Category(models.Model):
    description= models.CharField(max_length=20)
    dflt_units = models.ForeignKey(ItemUnit, on_delete=models.CASCADE)
    inactive = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.description

class Tax(models.Model):
    CHOICES = (
        (0,'No'),
        (1,'Yes')
    )
    name = models.CharField(max_length=200)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2)
    excempt = models.BooleanField(choices=CHOICES, default=False)
    default = models.BooleanField(max_length=9, choices=CHOICES, default = False)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name


class StockMaster(models.Model):
    stock_id = models.CharField(max_length=50, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tax_type = models.ForeignKey(Tax, on_delete=models.CASCADE)
    description = models.TextField(max_length=50)
    long_description = models.TextField()
    units = models.ForeignKey(ItemUnit, on_delete=models.CASCADE)
    inactive = models.BooleanField(default=False)
    deleted_status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.description

class Item(models.Model):
    description = models.CharField(max_length=200,db_index=True)
    stock_id = models.CharField(max_length=50, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.FileField(upload_to='uploads/item_image')
    inactive = models.BooleanField(default=False)
    deleted_status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.description


class Preference(models.Model):
    category=models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

class StockTransfer(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    source = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    note = models.TextField()
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    transfer_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Location(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    Email = models.EmailField()
    phone = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name


