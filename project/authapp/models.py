from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    # TODO FIX not unique emails
    """
    Additional fields to a User model
    """
    phone_validator = RegexValidator(regex=r'^\+\d{5,16}$',
                                     message="Format: +79001234567  (min 5, max 16 digits)")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False, blank=False)
    phone = models.CharField(max_length=16, blank=True, validators=[phone_validator], verbose_name="Phone number")

    def __str__(self):
        return f'Profile obj for User {self.user}'



