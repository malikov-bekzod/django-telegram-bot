from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=30, null=False)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='addresses')
    name = models.CharField(max_length=40, null=False)

    class Meta:
        db_table = 'address'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)
    homework = models.TextField(null=False)

    class Meta:
        db_table = 'lesson'

    def __str__(self):
        return self.title


class Module(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='modules')

    class Meta:
        db_table = 'modules'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    module = models.ManyToManyField(Module, related_name='courses')
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.name


class PayType(models.Model):
    type = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'pay_type'

    def __str__(self):
        return self.type


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount = models.IntegerField(null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments')
    type = models.ForeignKey(PayType, on_delete=models.CASCADE, related_name='payments')

    class Meta:
        db_table = 'payments'

    def __str__(self):
        return f'Payment {self.id}'


class ProductsUser(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'products_user'
        verbose_name = 'Product User'
        verbose_name_plural = 'Product Users'
        ordering = ['id']


class ProductsProduct(models.Model):

    # Mahsulot kategoriyasi
    category_code = models.CharField(max_length=20)
    category_name = models.CharField(max_length=50)

    # Mahsulot kategoriya ichida ketgoriyasi ("Go'sht"->"Mol go'shti")
    subcategory_code = models.CharField(max_length=20)
    subcategory_name = models.CharField(max_length=50)

    # Mahsulot haqida malumot
    productname = models.CharField(max_length=50)
    photo = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField()
    description = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.productname

    class Meta:
        db_table = 'products_product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']
