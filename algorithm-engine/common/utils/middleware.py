"""
django中间件
"""
import json

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from common.utils.request_util import get_request_user, get_request_ip, get_request_data, get_request_path, get_os, \
    get_browser, get_verbose_name


class ApiLoggingMiddleware(MiddlewareMixin):
    """
    用于记录API访问日志中间件
    """

    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.enable = getattr(settings, 'API_LOG_ENABLE', None) or False
        self.methods = getattr(settings, 'API_LOG_METHODS', None) or set()
        self.operation_log_id = None

    @classmethod
    def __handle_request(cls, request):
        # TODO 这里可以拓展request对象，为了方便__handle_response记录更多的信息（审计）
        pass

    def __handle_response(self, request, response):
        # TODO 这里可以记录返回的日志（审计）
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(view_func, 'cls') and hasattr(view_func.cls, 'queryset'):
            if self.enable:
                if self.methods == 'ALL' or request.method in self.methods:
                    # TODO 这里可以记录视图相关的日志（审计）
                    pass
        return

    def process_request(self, request):
        self.__handle_request(request)

    def process_response(self, request, response):
        """
        主要请求处理完之后记录
        :param request:
        :param response:
        :return:
        """
        if self.enable:
            if self.methods == 'ALL' or request.method in self.methods:
                self.__handle_response(request, response)
        return response


def process_response(request, response):
    return response


class ApiSecurityMiddleware(MiddlewareMixin):
    """
    用于API安全中间件
    """

    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.enable = getattr(settings, 'API_SECURITY_ENABLE', None) or True

    def __handle_request(self, request):
        if self.enable:
            if request.path.startswith('/api/fuc/'):  # 仅拦截功能API
                # TODO 这里编写API验签算法

                # print(request.__dict__.items())
                pass

        pass

    def process_request(self, request):
        self.__handle_request(request)
