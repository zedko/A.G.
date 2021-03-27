from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
import logging

from .models import Profile
from .forms import CustomizedUserCreationForm, PasswordResetCustomForm

logger = logging.getLogger(__name__)


def success(request):
    context = dict()
    context['previous_page'] = request.META.get('HTTP_REFERER')
    return render(request, template_name='authapp/success.html', context=context)


class UserCreateView(FormView):
    """
    Registration form (creates User and Profile)
    """
    model = User
    template_name = 'authapp/basic_form.html'
    form_class = CustomizedUserCreationForm
    success_url = reverse_lazy('adminapp:admin_index')

    def form_valid(self, form):
        try:
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            Profile.objects.create(
                user=user,
                phone=form.cleaned_data['phone']
            )
            login(self.request, user)
        except Exception as e:
            logger.error(f"Error with User registration {e}")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_button'] = 'Register'
        return context


class LoginFormView(LoginView):
    """
    Login Form
    """
    template_name = 'authapp/basic_form.html'
    success_url = reverse_lazy('adminapp:admin_index')
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_button'] = 'Log in!!!'
        context['reset_password_link'] = True
        return context


class PasswordCustomResetView(PasswordResetView):
    """
    Password change via email
    """
    form_class = PasswordResetCustomForm
    template_name = 'authapp/basic_form.html'
    email_template_name = 'authapp/emails/password_reset_email.html'
    success_url = reverse_lazy('authapp:success')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_button'] = 'Reset password'
        return context


class PasswordResetConfirmCustomView(PasswordResetConfirmView):
    template_name = 'authapp/basic_form.html'
    success_url = reverse_lazy('authapp:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_button'] = 'Reset password'
        return context


def logout_view(request):
    logout(request)
    return redirect('authapp:login')





