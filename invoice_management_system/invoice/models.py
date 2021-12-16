from django.db import models

# Create your models here.


class Invoice(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, null=False)
    invoice_id = models.IntegerField(null=False, blank=False)
    invoice_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=False, blank=False)
    name = models.CharField('Customer Name', max_length=30, null=False)
    address = models.CharField(max_length=30, default='downtown', null=True)

    line_one = models.CharField('Line One', max_length=30, default='', null=True, blank=True)
    line_one_quantity = models.IntegerField('Quantity', null=True, blank=True, default= 0)
    line_one_unit_price = models.IntegerField('Unit Price (D)', default=0, null=True, blank=True)
    line_one_total_price = models.IntegerField('Total Price (D)', default= 0 , null=True, blank=True)

    phone_number = models.CharField(max_length=15, null=False, blank=False)
    total = models.IntegerField(default=0, null=True, blank=True)
    balance = models.IntegerField(default=0, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
    paid = models.BooleanField(default=False)

    invoice_type_list =(
        ('Receipt','Receipt'),
        ('perform invoice','perform invoice'),
        ('invoice', 'invoice')
    )
    invoice_type = models.CharField(max_length=20, null=True, blank=True, choices=invoice_type_list)

    def __str__(self):
        return self.name





