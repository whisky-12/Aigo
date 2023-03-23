import subprocess
import logging

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.request import Request

from common.utils.json_response import DetailResponse

logger = logging.getLogger(__name__)


class XxxView(APIView):
    """
    示例API
    """

    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        responses={"200": openapi.Response("获取成功")},
        security=[],
        tags=["algorithm"],
        operation_id="xxx",
        operation_description="xxx算法",
    )
    def post(self, request: Request):

        # 获取URL查询参数
        print(request.query_params)

        # 获取BODY查询参数
        print(request.data)

        param1: str = request.data['param1']

        # print(request.__dict__.items())
        python_path = '/Users/zaki/opt/anaconda3/envs/algorithm-yolov/lib/python3.8'
        sh = [
            "echo ?????? |sudo -S",
            python_path,
            "/Users/zaki/work/workspace/standard/ai/algorithm/algorithm-engine/fuc/algorithm/feature/yolov/main.py",
            "--param1", param1
        ]

        proc = subprocess.Popen(sh,
                                bufsize=0,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True,
                                shell=True,
                                env={"PATH": python_path}
                                )

        nextline: str = ''
        try:
            while True:
                nextline = proc.stdout.readline()
                print(nextline.strip())
                if not subprocess.Popen.poll(proc) is None:
                    if nextline == "":
                        break
        except Exception as e:
            logging.error(e)
        finally:
            proc.stdout.close()

        return DetailResponse(data=nextline)

