from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, forms

from authapp.models import Profile


class UserUpdateCustomForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateCustomForm(forms.ModelForm):
    # phone = forms.CharField(max_length=16, validators=[Profile.phone_validator])
    class Meta:
        model = Profile
        fields = ['phone']
