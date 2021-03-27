import logging

from django.http import HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

from .serializers import UserSerializer

logger = logging.getLogger(__name__)


@login_required
def generate_api_token(request):
    """
    Generating new API token
    """
    user = request.user
    Token.objects.filter(user=user).delete()
    Token.objects.update_or_create(user=user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@api_view(['GET'])
def method_rest_api_po_zaprosu_s_secret_kluchom(request):
    """
    Которая просто отдает имя и email аккаунта  :)
    """
    serializer = UserSerializer(request.user)
    return JsonResponse(serializer.data)

