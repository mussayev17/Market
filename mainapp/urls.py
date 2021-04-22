from django.urls import path
from django.contrib.auth.views import LogoutView
from .decorators import check_recaptcha
from . import views
from django.views.decorators.cache import cache_page
from django.contrib.auth import views
from django.conf.urls import url


from .views import (
    BaseView,
    ProductDetailView,
    CategoryDetailView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    LoginView,
    RegistrationView, ProfileView,SearchResultsView,
    PayedOnlineOrderView
)


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', LoginView.as_view(), name='login'),
path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('payed-online-order/', PayedOnlineOrderView.as_view(), name='make_order'),

]

