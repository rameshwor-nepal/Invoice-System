from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_id', 'name','address','phone_number','invoice_date','total','paid','invoice_type']


    def clean_invoice_id(self):
        invoice_id = self.cleaned_data.get('invoice_id')
        if not invoice_id:
            raise forms.ValidationError('This field is required')
        return invoice_id


    def clean_name(self):
            name = self.cleaned_data.get('name')
            if not name:
                raise forms.ValidationError('This field is required')
            return name


class InvoiceSearchForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['invoice_id', 'name']