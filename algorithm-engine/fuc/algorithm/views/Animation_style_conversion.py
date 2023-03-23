import logging

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.request import Request

from common.utils.json_response import DetailResponse

from fuc.algorithm.feature.Image2Image.Animation_style_conversion.main import stylepro_artistic

logger = logging.getLogger(__name__)

class Animation_style_conversion_View(APIView):
    """
    示例API
    """

    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        responses={"200": openapi.Response("获取成功")},
        security=[],
        tags=["algorithm"],
        operation_id="Categorization_of_dishes",
        operation_description="Categorization_of_dishes工程",
    )
    def post(self, request: Request):

        # 获取URL查询参数
        print(request.query_params)

        # 获取BODY查询参数
        print(request.data)

        content_imagePath: str = request.data['content_imagePath']
        styles_imagePath: str = request.data['styles_imagePath']
        # alpha: float = request.data['alpha']
        alpha: float = 0.5

        result: str = stylepro_artistic(content_imagePath, styles_imagePath, alpha)
        return DetailResponse(data=result)