import os
import uuid
from uuid import uuid4

from address.models import AddressField
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


def user_photo_file_path(_instance, filename):
    """Generate file path for a new user photo"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("upload/user/", filename)


def create_new_address():
    pass


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        address=None,
        password=None,
        **extra_fields,
    ):
        """Create and save a new user"""
        if not email:
            raise ValueError("Email adresse is compulsory!")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # for multiple dbs we use using=self._db
        user.save(using=self._db)
        if address:
            new_address = create_new_address(address)
            if new_address:
                user.address1 = new_address
                print(new_address)
                user.save(using=self._db)
        user.save(using=self._db)
        # create device
        return user

    def create_superuser(self, email, password):
        """Create and saves a new superuser"""
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    GENDER = [("Male", "Male"), ("Female", "Female")]

    username = models.CharField(default="", max_length=50, blank=True)
    identifier = models.CharField(default=uuid4, max_length=50, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=30, choices=GENDER, null=True)
    birth_date = models.DateField(null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(null=True, blank=True, unique=True, max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    address = AddressField(blank=True, null=True, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to=user_photo_file_path)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email
