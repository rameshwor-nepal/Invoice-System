from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Invoice
from .forms import InvoiceForm, InvoiceSearchForm

# Create your views here.

def index(request):
    invoice = Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)
    context = {'invoice':invoice,
                'form':form
                }
    

    if request.method == 'POST':
        invoice = Invoice.objects.filter(invoice_id__icontains=form['invoice_id'].value(),
                                        name__icontains=form['name'].value()
                                        )
        context = {
        "form": form,
        "invoice": invoice,
    }

    return render(request,  'invoice_data.html', context=context)
    


def add(request):
    form = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST or None)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
        return redirect('index')

    context = {'form':form}
    return render (request, 'form.html', context=context)


def updateinvoice(request, id):
    invoice = Invoice.objects.get(pk=id)
    form = InvoiceForm(request.POST or None, instance=invoice)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {'form':form}
    return render (request, 'update.html', context=context)


def deleteinvoice(request, id):
    invoice = Invoice.objects.get(pk=id)
    invoice.delete()
    return redirect ('index')
    