from django.contrib import admin
from .models import ProductsProduct, ProductsUser, City, Address, Lesson, Module, Course, PayType, Payment

admin.site.register([ProductsProduct, ProductsUser, City, Address, Lesson, Module, Course, PayType, Payment])
