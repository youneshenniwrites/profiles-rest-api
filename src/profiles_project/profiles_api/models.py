from django.db import models
from django.contrib.auth.models import (
                                        AbstractBaseUser,
                                        PermissionsMixin,
                                        BaseUserManager
                                        )


class UserProfileManager(BaseUserManager):
    """
    helps Django works with our custom user model.019
    """

    def create_user(self, email, name, password=None):
        """
        Creates a new user profile object.
        """

        if not email:
            raise ValueError('You must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)  # creates a new user model object

        user.set_password(password)  # password hashing
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves the admin."""

        admin = self.create_user(email, name, password)

        admin.is_superuser = True
        admin.is_staff = True

        admin.save(using=self._db)

        return admin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a custom user profile inside our system. 018
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Used to get users full names.
        """

        return self.name

    def get_short_name(self):
        """
        Used to get users short names.
        """

        return self.name

    def __str__(self):
        """
        Django uses this to convert the object to a string.
        """

        return self.email
