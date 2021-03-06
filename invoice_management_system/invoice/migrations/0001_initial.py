# Generated by Django 3.2.3 on 2021-06-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('invoice_id', models.IntegerField()),
                ('invoice_date', models.DateTimeField()),
                ('name', models.CharField(max_length=30, verbose_name='Customer Name')),
                ('address', models.CharField(default='downtown', max_length=30, null=True)),
                ('line_one', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Line One')),
                ('line_one_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity')),
                ('line_one_unit_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)')),
                ('line_one_total_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Total Price (D)')),
                ('phone_number', models.CharField(max_length=15)),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('balance', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('invoice_type', models.CharField(blank=True, choices=[('Receipt', 'Receipt'), ('perform invoice', 'perform invoice'), ('invoice', 'invoice')], max_length=20, null=True)),
            ],
        ),
    ]
