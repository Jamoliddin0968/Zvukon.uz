from django.db import models
import os
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib import auth


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):

        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)

    def create_user(self, username,  password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


def rename_user_image(instance, filename):
    upload_to = 'user'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class User(AbstractBaseUser, PermissionsMixin):
    """
    telefon raqam va parol majburiy . qolgan filedlar ixtiyoriy
    """
    username = models.CharField(_("Telefon raqam"), max_length=255, unique=True, error_messages={
                                    "unique": _("Bu raqam bo'yicha foydalanuvchi mavjud"), })
    adress = models.CharField(_("Manzil"), max_length=127)
    img = models.ImageField(
        _("Profil rasm"), upload_to=rename_user_image, null=True, blank=True)

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    # telegram_link = models.CharField(max_length=150, null=True)
    # instagram_link = models.CharField(max_length=150, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        _("date joined"), default=timezone.now)

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    objects = CustomUserManager()
    USERNAME_FIELD = "username"

    class Meta:
        # db_table = "Foydalanuvchi"
        verbose_name = _("Foydalanuvchi")
        verbose_name_plural = _("Foydalanuvchilar")
        
class Account(models.Model):
    TELEGRAM,PHONE_NUMBER,INSTAGRAM = (
        "Telegram","Phone Number","Instagram"
    )
    SOCIAL = [
        (TELEGRAM,TELEGRAM),
        (PHONE_NUMBER,PHONE_NUMBER),
        (INSTAGRAM,INSTAGRAM)
    ]
    
    name = models.CharField(_("Ijtimoiy tarmoq"),max_length=15,choices=SOCIAL)
    link = models.CharField(_("link"),max_length=255)