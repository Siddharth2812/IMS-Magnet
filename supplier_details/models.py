from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Supplier(models.Model):
    sl_no = models.AutoField(primary_key=True, verbose_name="SLNO")
    supplier_name = models.CharField(max_length=255, verbose_name="SUPPLIER NAME")
    address_line1 = models.CharField(max_length=255, verbose_name="ADDRESS 1", blank=True)
    address_line2 = models.CharField(max_length=255, verbose_name="ADDRESS 2", blank=True)
    address_line3 = models.CharField(max_length=255, verbose_name="ADDRESS 3", blank=True)
    address_line4 = models.CharField(max_length=255, verbose_name="ADDRESS 4", blank=True)
    state = models.CharField(max_length=100, verbose_name="STATE")
    state_code = models.CharField(max_length=10, verbose_name="STATE CODE")
    payment_terms = models.CharField(max_length=255, verbose_name="Payment Terms", blank=True)
    pan_no = models.CharField(max_length=10, verbose_name="PAN NO")
    gst_no = models.CharField(max_length=15, verbose_name="GST NO")
    igst = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="I GST", 
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    cgst = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="C GST", 
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    sgst = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="S GST", 
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    total_gst = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="TOTAL GST", 
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    contact_person = models.CharField(max_length=255, verbose_name="CONTACT PERSON", blank=True)
    phone_no = models.CharField(max_length=20, verbose_name="PHONE NO", blank=True)
    email = models.EmailField(verbose_name="E-MAIL", blank=True)
    bank_name = models.CharField(max_length=255, verbose_name="BANK NAME", blank=True)
    branch = models.CharField(max_length=255, verbose_name="BRANCH", blank=True)
    account_no = models.CharField(max_length=50, verbose_name="ACC NO", blank=True)
    ifsc_code = models.CharField(max_length=11, verbose_name="IFSC CODE", blank=True)
    email_1 = models.EmailField(verbose_name="E-MAIL - 1", blank=True)
    vendor_code = models.CharField(max_length=50, verbose_name="VENDOR CODE", unique=True)

    def __str__(self):
        return f"{self.sl_no} - {self.supplier_name}"

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        ordering = ['sl_no']
