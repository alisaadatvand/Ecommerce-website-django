from django.db import models
from django.urls import reverse
from category.models import Category
from teacher.models import Teacher

# Create your models here.

class Product(models.Model):
    product_name = models.CharField((" نام محصول "),max_length=2000, unique=True)
    slug = models.SlugField(max_length=2000, unique=True)
    description = models.IntegerField((" مدت زمان دوره"), blank=True, help_text=" ساعت ")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.TextField((" تاریخ دوره "),max_length=200,blank=True)
    reg_date = models.TextField((" مهلت ثبت نام "),max_length=200,blank=True)
    full_description = models.TextField((" توضیحات "),max_length=20000, blank=True)
    price = models.IntegerField((" قیمت "),help_text=" تومان ")
    images = models.ImageField((" تصویر "),upload_to='photos/product')
    stock = models.IntegerField((" ظرفیت "))
    is_available = models.BooleanField((" فعال "),default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField((" تاریخ ایجاد "),auto_now_add=True)
    modified_date = models.DateTimeField((" تاریخ آخرین تغیر "),auto_now=True)
    

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class StockProduct(models.Model):
        name = models.ForeignKey(Product, on_delete=models.CASCADE)
        Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField((" ظرفیت "),default=20) 

        def __str__(self):
          return f'{self.name} {self.Teacher}'