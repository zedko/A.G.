import logging

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from rest_framework.authtoken.models import Token


from authapp.models import Profile
from .forms import UserUpdateCustomForm, ProfileUpdateCustomForm
from api.models import LogApiRequestsModel

logger = logging.getLogger(__name__)


@login_required
def admin_index_view(request):
    context = {}
    context['users'] = User.objects.all()
    context['token'] = Token.objects.filter(user=request.user).first()
    context['api_requests_logs'] = LogApiRequestsModel.objects.all()

    logger.debug(f'{request.user} is logged in {context}')

    return render(request, 'adminapp/base.html', context)


@user_passes_test(lambda u: u.is_staff, login_url='adminapp:admin_index', redirect_field_name=None)
def user_update_view(request, pk: int):
    user = User.objects.get(pk=pk)

    # create profile if not exists for some reason
    try:
        user.profile
    except Profile.DoesNotExist as e:
        Profile(user=user)

    if request.method == 'POST':
        u_form = UserUpdateCustomForm(request.POST, instance=user)
        p_form = ProfileUpdateCustomForm(request.POST, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Update successful!')
            return redirect('adminapp:admin_index')
    else:
        u_form = UserUpdateCustomForm(instance=user)
        p_form = ProfileUpdateCustomForm(instance=user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'owner': user,
    }

    return render(request, 'adminapp/update_profile.html', context)


