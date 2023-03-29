from django.db import models
import os
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib import auth




