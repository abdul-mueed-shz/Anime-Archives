from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from apps.common.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, user_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            user_name=user_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    user_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'user_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Right(BaseModel):
    name = models.CharField(max_length=300, unique=True, blank=False, null=False)


class Role(BaseModel):
    name = models.CharField(max_length=300, unique=True, blank=False, null=False)
    rights = models.ManyToManyField(Right, related_name='right', blank=False)


class UserRole(BaseModel):
    user = models.ManyToManyField(User, related_name='user_role')
    role = models.ManyToManyField(Role, related_name='right')
