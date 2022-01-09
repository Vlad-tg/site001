from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView
from .models import *
from .mixins import CartMixins
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AnonymousUser
from .form import *
from django.db.models import Count, Sum, F, Prefetch
from django.db.models.functions import Lower
from .utils import recalc_cart
from django.db.models import Q
from django.contrib import messages


# -------------------------------------------------------------------------------------------- #

class TestThreeViews(DetailView):
    def get(self, request, *args, **kwargs):
        form = TestForm(request.POST or None)
        context = {
            'form': form

        }
        return render(request, 'main/(NONE)test_three.html', context)


class TestTwoViews(DetailView):
    def get(self, request, *args, **kwargs):
        films = Product.objects.filter(id=1).values('id', 'title')
        tests = Product.objects.values('title').exclude(title="Tour in Japane")
        mail = Product.objects.annotate(Count('title')).order_by('title')
        aris = Product.objects.values('pub_date')
        qs1 = Product.objects.values('title')
        qs2 = Country.objects.values('name')
        reds = qs1.union(qs2)
        pp = Product.objects.extra(where=["pub_date > '2021-11-15'"])
        sets = Product.objects.extra(where=['title=%s'], params=['Japane'])
        lefts = Product.objects.filter(title__iendswit='en')

        context = {
            'films': films,
            'tests': tests,
            'mail': mail,
            'aris': aris,
            'reds': reds,
            'lefts': lefts,



        }
        return render(request, 'main/(NONE)test_two.html', context)


class TestView(DetailView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        actives = Product.objects.all().filter(status='Active')
        inactive = Product.objects.all().filter(status='Inactive')
        counts = Product.objects.all()

        context = {
            'products': products,
            'actives': actives,
            'inactive': inactive,
            'counts': counts,


        }
        return render(request, 'main/add_cart_002.html', context)
# -------------------------------------------------------------------------------------------- #


class MainPageViews(TemplateView):
    template_name = "main/main_page.html"


class AddToCartView(CartMixins, View):

    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, product=product

        )
        if created:
            self.cart.products.add(cart_product)
        qty_children = int(request.GET.get('qty_children'))
        qty_adult = int(request.GET.get('qty_adult'))

        cart_product.qty_children = qty_children
        cart_product.qty_adult = qty_adult
        cart_product.save_one()
        recalc_cart(self.cart)
        # messages.add_message(request, messages.INFO, "Product added successfully")
        return HttpResponseRedirect('/cart/')


class CartView(CartMixins, View):

    def get(self, request, *args, **kwargs):
        context = {
            'cart': self.cart

        }
        return render(request, 'main/cart.html', context)


class DeleteFromCartView(CartMixins, View):

    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, product=product
        )
        self.cart.products.remove(cart_product)
        cart_product.delete()
        recalc_cart(self.cart)
        # messages.add_message(request, messages.INFO, "Product added successfully")
        return HttpResponseRedirect('/cart/')


class ChangeQTYCartView(CartMixins, View):

    def post(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, product=product
        )
        qty = int(request.POST.get('qty'))
        cart_product.qty = qty
        cart_product.save()
        recalc_cart(self.cart)
        # messages.add_message(request, messages.INFO, "Product added successfully")
        return HttpResponseRedirect('/cart/')


class LoginView(CartView, View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'cart': self.cart
        }

        return render(request, 'main/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {'form': form, 'cart': self.cart}
        return render(request, 'main/login.html', context)


class RegistrationView(CartView, View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'cart': self.cart
        }

        return render(request, 'main/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form,
            'cart': self.cart
        }
        return render(request, 'main/registration.html', context)
