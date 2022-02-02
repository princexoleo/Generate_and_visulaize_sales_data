from django.db import models
from django.shortcuts import reverse
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code

# Create your models here.
class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = ("Position")
        verbose_name_plural = ("Positions")

    def __str__(self):
        return f"id: {self.id}, product: {self.product}, quantity: {self.quantity}, price: {self.price}"

    def get_absolute_url(self):
        return reverse("Position_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)
    
    def get_sales_id(self):
        sale_obj = self.sale_set.first()
        return sale_obj.id
        


# Sales model class
class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = ("Sale")
        verbose_name_plural = ("Sales")

    def __str__(self):
        return f"Sales for the amount of ${self.total_price}"

    def get_absolute_url(self):
        return reverse("sales:sale_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if self.transaction_id =="":
            self.transaction_id = generate_code()
        if self.created_at == None:
            self.created_at = timezone.now()
        if self.updated_at == None:
            self.updated_at = timezone.now()
        
        return super().save(*args, **kwargs)
    
    def get_positions(self):
        return self.positions.all()


# A CSV class model
class CSV(models.Model):
    file_name = models.CharField(max_length=120)
    csv_file = models.FileField(upload_to='csvs/', null=True)
    #activated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("CSV")
        verbose_name_plural = ("CSVs")

    def __str__(self):
        return str(self.file_name)

    def get_absolute_url(self):
        return reverse("CSV:CSV_detail", kwargs={"pk": self.pk})