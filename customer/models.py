from django.db import models


# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(max_length=30)
    address = models.TextField(blank=True)
    contact = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    inactive = models.BooleanField(default = False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
