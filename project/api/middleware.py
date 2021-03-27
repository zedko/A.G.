import logging

from .models import LogApiRequestsModel

logger = logging.getLogger(__name__)


class LogApiRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if 'api' in request.path:
            LogApiRequestsModel.objects.create(user=request.user.username, url=request.path)
            logger.debug(f'MIDDLEWARE REQUEST ADDED LOG {request.user.username}, {request.path}')
        return response
