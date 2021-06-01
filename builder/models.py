from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import string
import random


def uid():
    length = 7
    user_uid = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(user_uid, k=length))
        if User.objects.filter(user_sid=code).count() == 0:
            break
    return code


def cid():
    length = 7
    user_cid = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(user_cid, k=length))
        if User.objects.filter(user_cid=code).count() == 0:
            break
    return code


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(verbose_name="Email", max_length=70, unique=True)
    user_sid = models.CharField(verbose_name="UID", default=uid, max_length=8, unique=True, editable=False)
    user_cid = models.CharField(verbose_name="UCheckID", default=cid, max_length=8, unique=True, editable=False)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_pro = models.BooleanField(verbose_name="Pro User", default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
