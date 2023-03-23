from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from common.utils.json_response import DetailResponse


class SignLogin(APIView):
    """
    接口文档的验签接口
    """

    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        security=[],
        tags=["security"],
        operation_id="验证签名",
        operation_description="验证API签名",
    )
    def post(self, request):
        print("=================")
        return DetailResponse(data={})

