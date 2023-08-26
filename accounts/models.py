from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('کاربر حتما باید ایمیل داشته باشد')
        if not username:
            raise ValueError('کاربر حتما باید نام کاربری داشته باشد')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)

class Account(AbstractBaseUser):
    first_name = models.CharField((' نام '),max_length=50)
    last_name = models.CharField((' نام خانوادگی ' ),max_length=50)
    username = models.CharField((' نام کاربری '),max_length=10, unique=True)
    email = models.EmailField((' ایمیل '),max_length=100, unique=True)
    phone_number = models.CharField((' شماره موبایل '),max_length=50)

    # required
    date_joined = models.DateTimeField((' تاریخ ثبت نام '),auto_now_add=True)
    last_joined = models.DateTimeField((' تاریخ آخرین ورود '),auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True