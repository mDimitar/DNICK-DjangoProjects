from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.URLField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Sale Model
class Sale(models.Model):
    products = models.ManyToManyField(Product, through='SaleItem')
    sale_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self):
        return f"Sale #{self.pk}"

# SaleItem Model (through table for the many-to-many relationship)
class SaleItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name

# Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"