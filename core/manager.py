from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.password_validation import validate_password

from django.core.exceptions import ValidationError

from rest_framework.exceptions import ValidationError as DRFValidationError
import json

class UserManager(BaseUserManager):
    use_in_migrations = True




    def create_user(self, password=None, **extra_fields):




        try:

            validate_password(password)
        except ValidationError as e:

            raise DRFValidationError({'detail': list(e)[0]})
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



    def update_user(self, user_id, **kwargs):

            try:

                validate_password(kwargs['password'])
            except ValidationError as e:

                raise DRFValidationError({'detail': list(e)[0]})


            user = self.get(id=user_id)

            for attr, value in kwargs.items():
                setattr(user, attr, value)
            user.set_password(kwargs['password'])

            user.save(using=self._db)

            return user
