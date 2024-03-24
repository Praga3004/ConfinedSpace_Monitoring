from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password,name,email,number,birthdate,addres,gender,country,city ):
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            full_name=name,
            email=email,
            phone_number=number,
            birth_date=birthdate,
            gender=gender,
            street_address=addres,
            country=country,
            city=city
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=100,default='')
    email = models.EmailField(unique=True,default='')
    phone_number = models.CharField(max_length=15,default='')
    birth_date = models.DateField(default='1900-01-01')
    gender = models.CharField(max_length=10,default='')
    street_address = models.CharField(max_length=255,default='')
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50,default='')

    objects = CustomUserManager()  # You can use the same manager as CustomUser if needed

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
