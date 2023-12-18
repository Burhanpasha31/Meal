from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid 

class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, name, password=None):
        if not email or not phone or not name:
            raise ValueError("Users must have an email address, phone, and name")

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            name=name,
        )

        user.set_password(password)
        user.email_verified = True

        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, name, password=None):
        user = self.create_user(
            email,
            password=password,
            phone=phone,
            name=name,
        )
        user.is_admin = True
        user.email_verified = True
        user.phone_verified = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    image = models.ImageField("user_image", null=True, blank=True)

    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class is_seller(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    class Meta:
        app_label = 'account'

    def __str__(self):
        return self.name


class is_customer(models.Model):
    seller = models.ForeignKey(is_seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, default='')
    cost = models.IntegerField()
    phone = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name
