from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from User.manager import UserManager


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=70, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    point = models.DecimalField(max_digits=10, decimal_places=2, default=25.00)

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("customer", "Customer"),
        ("vendor", "Vendor"),
        ("staff", "Staff"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone_number"]

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    whatsapp_number = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    GENDER = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHER", "OTHER"),
    )
    date_of_birth = models.DateField(blank=True, null=True, default=datetime.now)
    sex = models.CharField(choices=GENDER, max_length=10, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile/%y/%m", blank=True, null=True
    )
    last_open = models.DateTimeField(blank=True, null=True, auto_now=True)
