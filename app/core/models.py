from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import os, uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class UserManager(BaseUserManager):

    def create_buyer(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_buyer = True
        user.is_seller=False
        user.is_staff=False
        user.is_superuser=False
        user.save(using=self._db)
        return user
    
    def create_seller(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_buyer = False
        user.is_seller = True
        user.is_staff=False
        user.is_superuser=False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_buyer = True
        user.is_seller = False
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_buyer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    cart_list = models.ManyToManyField('Item')
    USERNAME_FIELD = 'email'

    objects = UserManager()

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    unit_number = models.CharField(max_length=255)

class FinancialDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    merchant_account = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


def item_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/item_pictures/', filename)


class Item(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits= 10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True, upload_to=item_image_file_path)
    uploaded_date = models.DateField(auto_now_add=True)    
    in_stock = models.BooleanField(default=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField(max_length=1000)


    
    

