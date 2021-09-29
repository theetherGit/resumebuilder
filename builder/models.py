from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import string
import random
from django.conf import settings

CustomUser = settings.AUTH_USER_MODEL

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

def ruid():
    length = 5
    resume_uid = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(resume_uid, k=length))
        if ResumeTemplate.objects.filter(resume_uid=code).count() == 0:
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


class Type(models.Model):
    type = models.CharField(verbose_name="Type", max_length=20, unique=True)
    objects = models.Manager()


class ResumeTemplate(models.Model):
    resume_name = models.CharField(verbose_name="Template Name", max_length=255, unique=True)
    resume_image = models.ImageField(verbose_name="Resume Image")
    resume_uid = models.CharField(verbose_name="R_UID", default=ruid, max_length=8, unique=True, editable=False)
    resume_type = models.CharField(verbose_name="Type", editable=False, max_length=15)
    objects = models.Manager()


class PersonDetail(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    name = models.CharField(verbose_name="Person Name", max_length=100)
    address = models.CharField(verbose_name="Address", max_length=255)
    email = models.EmailField(verbose_name="Email")
    contact = models.BigIntegerField(verbose_name="Contact")
    profile = models.URLField(verbose_name="Profile")


class PersonProfileImage(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    image = models.ImageField(verbose_name="Image")
    objects = models.Manager()


class PersonCareerObjective(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    aim = models.TextField(verbose_name="Objective")
    objects = models.Manager()
    

class PersonWorkExperience(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    name = models.CharField(verbose_name="Company Name", max_length=100)
    position = models.CharField(verbose_name="Position Name", max_length=100)
    duration = models.CharField(verbose_name="Working Period", max_length=100)
    city = models.CharField(verbose_name="City", max_length=100)
    details = models.TextField(verbose_name="Details")
    objects = models.Manager()
    
    
class PersonAcademicQualification(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    qualification = models.CharField(verbose_name="Qualification", max_length=255)
    institution = models.CharField(verbose_name="College/School", max_length=100)
    passed = models.IntegerField(verbose_name="Passing Year")
    city = models.CharField(verbose_name="City", max_length=100)
    objects = models.Manager()


class PersonCertificationCourse(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    name = models.CharField(verbose_name="Certificates Name", max_length=100)
    institution = models.CharField(verbose_name="Institution Name", max_length=100)
    year = models.IntegerField(verbose_name="Year")
    details = models.TextField(verbose_name="Details")
    objects = models.Manager()


class PersonProject(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    name = models.CharField(verbose_name="Project Name", max_length=200)
    details = models.TextField(verbose_name="Description")
    objects = models.Manager()


class PersonPosition(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    name = models.CharField(verbose_name="Name", max_length=255)
    place = models.CharField(verbose_name="Place", max_length=100)
    year = models.IntegerField(verbose_name="Year")
    details = models.TextField(verbose_name="Details")
    objects = models.Manager()


class PersonSkill(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    skill = models.CharField(verbose_name="Skill", max_length=255)
    objects = models.Manager()


class PersonHobbie(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    hobby = models.CharField(verbose_name="Hobby", max_length=255)
    objects = models.Manager()


class PersonKnownLanguage(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, editable=False)
    lang = models.CharField(verbose_name="Known Language", max_length=255)
    objects = models.Manager()
