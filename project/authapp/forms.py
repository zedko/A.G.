from django.contrib.auth.forms import UserCreationForm, forms, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

from .models import Profile


def no_user_by_email_validator(email):
    """
    Checks if there is no such user
    """
    if not User.objects.filter(email=email).exists():
        raise ValidationError(f"No user with email {email}")


class CustomizedUserCreationForm(UserCreationForm):
    """
    for User with Profile.phone creation
    """
    phone = forms.CharField(max_length=16, validators=[Profile.phone_validator])
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']


class PasswordResetCustomForm(PasswordResetForm):
    """
    Standard pass reset form but with validation
    """
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
        validators=[no_user_by_email_validator]
    )

