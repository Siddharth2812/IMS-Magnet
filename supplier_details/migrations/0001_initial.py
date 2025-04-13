# Generated by Django 5.1.6 on 2025-04-13 11:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('sl_no', models.AutoField(primary_key=True, serialize=False, verbose_name='SLNO')),
                ('supplier_name', models.CharField(max_length=255, verbose_name='SUPPLIER NAME')),
                ('address_line1', models.CharField(blank=True, max_length=255, verbose_name='ADDRESS 1')),
                ('address_line2', models.CharField(blank=True, max_length=255, verbose_name='ADDRESS 2')),
                ('address_line3', models.CharField(blank=True, max_length=255, verbose_name='ADDRESS 3')),
                ('address_line4', models.CharField(blank=True, max_length=255, verbose_name='ADDRESS 4')),
                ('state', models.CharField(max_length=100, verbose_name='STATE')),
                ('state_code', models.CharField(max_length=10, verbose_name='STATE CODE')),
                ('payment_terms', models.CharField(blank=True, max_length=255, verbose_name='Payment Terms')),
                ('pan_no', models.CharField(max_length=10, verbose_name='PAN NO')),
                ('gst_no', models.CharField(max_length=15, verbose_name='GST NO')),
                ('igst', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='I GST')),
                ('cgst', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='C GST')),
                ('sgst', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='S GST')),
                ('total_gst', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='TOTAL GST')),
                ('contact_person', models.CharField(blank=True, max_length=255, verbose_name='CONTACT PERSON')),
                ('phone_no', models.CharField(blank=True, max_length=20, verbose_name='PHONE NO')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-MAIL')),
                ('bank_name', models.CharField(blank=True, max_length=255, verbose_name='BANK NAME')),
                ('branch', models.CharField(blank=True, max_length=255, verbose_name='BRANCH')),
                ('account_no', models.CharField(blank=True, max_length=50, verbose_name='ACC NO')),
                ('ifsc_code', models.CharField(blank=True, max_length=11, verbose_name='IFSC CODE')),
                ('email_1', models.EmailField(blank=True, max_length=254, verbose_name='E-MAIL - 1')),
                ('vendor_code', models.CharField(max_length=50, unique=True, verbose_name='VENDOR CODE')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
                'ordering': ['sl_no'],
            },
        ),
    ]
