from tracemalloc import stop
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from accounts.models import *

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Name',
        validators=[
            MinLengthValidator(2, "Category Name must be greater than 2 characters")
        ],
    )

    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug',
        validators=[
            MinLengthValidator(2, "Category Slug must be greater than 2 characters")
        ],
    )

    description = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Description',
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On',
    )

    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated On',
    )

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = "Contact Us"

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField()


class Brand(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Name',
        validators=[
            MinLengthValidator(2, "Brand Name must be greater than 2 characters")
        ],
    )

    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug',
        validators=[
            MinLengthValidator(2, "Brand Slug must be greater than 2 characters")
        ],
    )

    description = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Description',
    )

    website = models.URLField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Website',
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On',
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Out of Stock', 'Out of Stock'),
    )

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        max_length=70,
        unique=True,
        verbose_name='Name',
        validators=[
            MinLengthValidator(5, "Product Name must be greater than 2 characters"),
        ],
    )

    slug = models.SlugField(
        max_length=70,
        unique=True,
        verbose_name='Slug',
        validators=[
            MinLengthValidator(5, "Product Slug must be greater than 2 characters"),
        ],
    )

    short_description = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Short Description',
    )

    long_description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Detailed Description',
        validators=[
            MaxLengthValidator(15000, "The value is too long."),
        ]
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=[
            MinValueValidator(0, "Price must be greater than 0."),
            MaxValueValidator(1_000_000, "Price must be less than 1000000."),
        ]
    )

    stock = models.IntegerField(
        verbose_name='Stock',
        validators=[
            MinValueValidator(0, "Stock must be greater than 0."),
            MaxValueValidator(5000, "Stock must be less than 5000."),
        ]
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Category',
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Brand',
    )

    image = models.ImageField(
        upload_to='products/images/',
    )

    status = models.CharField(
        max_length=25,
        choices=STATUS,
        default='Active',
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On',
    )

    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated On',
    )

    def __str__(self):
        return self.name


class Cart(models.Model):

    class Meta:
        verbose_name_plural = "Cart"
        unique_together = ['user', 'product']

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product',
    )

    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1,
        validators=[
            MinValueValidator(1, "Quantity must be greater than 0."),
            MaxValueValidator(5, "Quantity must be less than 5."),
        ]
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On',
    )