from django.db import models
from datetime import date
import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name='Name category', max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(verbose_name='Name country', max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    STATUS_TOUR_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    )
    title = models.CharField(verbose_name='Name', max_length=250)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category', verbose_name='Category', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Imagine')
    country = models.ForeignKey('Country', verbose_name='Country', on_delete=models.CASCADE)
    pub_date = models.DateField(verbose_name='Date', default=date.today)
    total_products = models.PositiveIntegerField(default=0)
    price_adult = models.DecimalField(verbose_name='Price for adult', decimal_places=2,
                                      max_digits=9, blank=True, null=True)
    price_children = models.DecimalField(verbose_name='Price for children', decimal_places=2,
                                         max_digits=9, blank=True, null=True)
    status = models.CharField(
        max_length=255,
        verbose_name='Status is order',
        choices=STATUS_TOUR_CHOICES,
        default=ACTIVE
    )
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return "{} : {}.".format(self.category.name, self.title)

    def get_model_name(self):
        return self.__class__.__name__.lower()

    def get_absolute_url(self):
        return reverse('test', kwargs={'slug': self.slug})


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Product, verbose_name='Name product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    qty_children = models.PositiveIntegerField(default=0)
    qty_adult = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')
    for_anonymous_user = models.BooleanField(default=False, verbose_name='AnonymousUser')

    def __str__(self):
        return "Product: {} (for Cart)".format(self.product.title)

    def save_one(self, *args, **kwargs):
        self.qty = self.qty_children + self.qty_adult
        self.total_price = (self.qty_adult * self.product.price_adult) + (self.qty_children * self.product.price_children)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.total_price = self.qty * (self.product.price_adult + self.product.price_children)
        super().save(*args, **kwargs)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', null=True, verbose_name='Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, default=0,  decimal_places=2, verbose_name='Total Price')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Customer', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Address', null=True, blank=True)

    def __str__(self):
        return "Customer: {} {}".format(self.user.first_name, self.user.last_name)

