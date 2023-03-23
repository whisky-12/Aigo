import logging

from django.contrib.auth.backends import ModelBackend

logger = logging.getLogger(__name__)


class CustomBackend(ModelBackend):
    """
    Django原生认证方式
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        print("============")
        # TODO 这里可以自定义认证方式
        pass
