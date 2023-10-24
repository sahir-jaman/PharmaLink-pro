from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from autoslug import AutoSlugField

from phonenumber_field.modelfields import PhoneNumberField

from versatileimagefield.fields import VersatileImageField

from common.models import BaseModelWithUid
from common.utils import get_email_slug


# user manageer
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser, BaseModelWithUid):
    email = models.EmailField(verbose_name="email address",max_length=255,unique=True)
    name = models.CharField(max_length=200)
    phone = PhoneNumberField(unique=True, null=True, blank=True)
    slug = AutoSlugField(populate_from=get_email_slug, unique=True)
    gender = models.CharField(max_length=10, blank=True)
    picture = VersatileImageField(upload_to='images', blank = True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # answer: All admins are staff
        return self.is_admin
