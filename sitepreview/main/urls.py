from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
  path('', MainPageViews.as_view(), name='home_page'),
  path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
  path('login/', LoginView.as_view(), name='login'),
  path('registration/', RegistrationView.as_view(), name='registration'),
  path('test/', TestView.as_view(), name='test'),
  path('cart/', CartView.as_view(), name='cart'),
  path('test_two/', TestTwoViews.as_view(), name='test_two'),
  path('test_three/', TestThreeViews.as_view(), name='test_three'),
  path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
  path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
  path('change-gty-cart/<str:slug>/', ChangeQTYCartView.as_view(), name='change_gty_cart'),
  path('login/', LoginView.as_view(), name='login'),
  path('registration/', RegistrationView.as_view(), name='registration'),

]
