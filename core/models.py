
from datetime import datetime
import uuid


from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _



from .manager import UserManager


def upload_path(instance, filname):
    now = datetime.now()
    date_time = now.strftime("%m%d%Y%H%M%S")
    return '/'.join([str(uuid.uuid4()),str(date_time), filname])


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30,unique=True)
    name = models.CharField(_('name'), max_length=30,default="amjad")
    sex = models.CharField(_('sex'), max_length=30,default="male")
    phone=models.CharField(_('phone'), max_length=30,default="099999")
    age=models.DateField()

    personal_id=models.FileField(upload_to=upload_path, blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')