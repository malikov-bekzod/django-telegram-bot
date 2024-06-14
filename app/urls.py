from django.contrib import admin
from django.urls import path, include
from .views import RegisterPageView, LessonPageView, LogoutPageView, LoginPageView, PayPageView, AddressView
from .views import ProductUserView, ProductPageView

urlpatterns = [
    path('course/', LessonPageView.as_view(), name='course'),
    path('payment/', PayPageView.as_view(), name='payment'),
    path('address/', AddressView.as_view(), name='address'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('users/', ProductUserView.as_view(), name='users'),

]
