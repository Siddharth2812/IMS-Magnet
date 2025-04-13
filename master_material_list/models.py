from django.db import models
from django.core.validators import MinValueValidator
from supplier_details.models import Supplier

class MasterMaterial(models.Model):
    CATEGORY_CHOICES = [
        # Add your category choices here
    ]
    
    SUB_CATEGORY_CHOICES = [
        # Add your sub-category choices here
    ]

    sl_no = models.AutoField(primary_key=True, verbose_name="SL.NO")
    vendor = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        verbose_name="VENDOR NAME",
        related_name='materials'
    )
    description = models.TextField(verbose_name="DESCRIPITION")  # Note: Original spelling preserved
    part_no = models.CharField(max_length=100, verbose_name="PART NO", unique=True)
    unit = models.CharField(max_length=50, verbose_name="UNIT")
    supplier_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="SUPPLIER RATE",
        validators=[MinValueValidator(0)]
    )
    seipl_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="SEIPL RATE",
        validators=[MinValueValidator(0)]
    )
    category = models.CharField(
        max_length=100,
        verbose_name="CATEGORY",
        choices=CATEGORY_CHOICES,
        blank=True
    )
    sub_category = models.CharField(
        max_length=100,
        verbose_name="SUB CATEGORY",
        choices=SUB_CATEGORY_CHOICES,
        blank=True
    )
    sale_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="SALE RATE",
        validators=[MinValueValidator(0)]
    )
    total_received_qty = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="TOTAL RECEIVED QTY",
        default=0,
        validators=[MinValueValidator(0)]
    )
    vendor_issued_qty = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="VENDOR ISSUED QTY",
        default=0,
        validators=[MinValueValidator(0)]
    )
    vendor_received_qty = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="VENDOR RECEIVED QTY",
        default=0,
        validators=[MinValueValidator(0)]
    )
    board_issue_qty = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="BOARD ISSUE QTY",
        default=0,
        validators=[MinValueValidator(0)]
    )
    avl_stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="AVL STOCK",
        default=0,
        validators=[MinValueValidator(0)]
    )
    avl_stock_value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="AVL STOCK VALUE",
        default=0,
        validators=[MinValueValidator(0)]
    )
    billing_qty_diff = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="BILLING QTY DIFF",
        default=0
    )
    total_received_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="TOTAL RECEIVED COST",
        default=0,
        validators=[MinValueValidator(0)]
    )
    total_billed_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="TOTAL BILLED COST",
        default=0,
        validators=[MinValueValidator(0)]
    )
    cost_diff = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="COST DIFF",
        default=0
    )

    def __str__(self):
        return f"{self.sl_no} - {self.part_no} ({self.description})"

    def save(self, *args, **kwargs):
        # Calculate derived fields before saving
        self.avl_stock = (
            self.total_received_qty +
            self.vendor_received_qty -
            self.vendor_issued_qty -
            self.board_issue_qty
        )
        self.avl_stock_value = self.avl_stock * self.supplier_rate
        self.billing_qty_diff = self.total_received_qty - self.board_issue_qty
        self.cost_diff = self.total_received_cost - self.total_billed_cost
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Master Material"
        verbose_name_plural = "Master Materials"
        ordering = ['sl_no']
        indexes = [
            models.Index(fields=['part_no']),
            models.Index(fields=['category', 'sub_category']),
        ]
