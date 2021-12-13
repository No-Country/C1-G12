from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ExtendUser(AbstractUser):
    is_patient = models.BooleanField('patient status', default=False)
    is_doctor = models.BooleanField('doctor status', default=False)
    is_sysadmin = models.BooleanField('sysadmin status', default=False)
    #password = models.CharField(max_length=50)

class Patient(models.Model):
    # Patient definition
    user = models.OneToOneField(ExtendUser, on_delete=models.CASCADE, primary_key=True)
    # Patient Fields
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    dni = models.CharField(max_length=15)
    age = models.DateField()
    gender = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    social = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)
    #USERNAME_FIELD = "username"
    #EMAIL_FIELD = "email"

class Doctor(models.Model):
    # Doctor definition
    user = models.OneToOneField(ExtendUser, on_delete=models.CASCADE, primary_key=True)
    # Doctor Fields
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    speciality = models.CharField(max_length=20)
    turn = models.CharField(max_length=15)

class SysAdmin(models.Model):
    user = models.OneToOneField(ExtendUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
