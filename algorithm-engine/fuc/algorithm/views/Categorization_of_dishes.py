import logging

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.request import Request

from common.utils.json_response import DetailResponse

from fuc.algorithm.feature.Image_classification.Categorization_of_dishes.main import mobilenet_v2_dishes

logger = logging.getLogger(__name__)


class Categorization_of_dishes_View(APIView):
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

        imagePath: str = request.data['imagePath']
        top_k: int = request.data['top_k']

        result: str = mobilenet_v2_dishes(imagePath,top_k)
        return DetailResponse(data=result)