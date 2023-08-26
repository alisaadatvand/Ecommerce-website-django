from django.db import models


# Create your models here.


class Teacher(models.Model):
    name = models.CharField((" نام و نام خانوادگی "),max_length=50 , blank=True)
    city = models.ForeignKey('City' , default='تهران' , on_delete=models.CASCADE)
    address = models.CharField((" آدرس "),max_length=50 , blank= True)
    phone = models.CharField((" شماره موبایل "),max_length=50 , blank=True) 
    degree = models.CharField((" مدرک تحصیلی ") ,max_length=50 , default='دکترا' ,choices=[('دیپلم','دیپلم'),
                                                                            ('لیسانس','لیسانس'),
                                                                            ('فوق لیسانس','فوق لیسانس'),
    ('دکترا','دکترا')])

    def __str__(self):
        return self.name
    




class City(models.Model):
    city = models.CharField((" شهر "),max_length=50,default="تهران")

    def __str__(self):
        return self.city
    
